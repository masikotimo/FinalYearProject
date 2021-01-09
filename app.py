
from Reports.SendReports import sendEmail,sendPassword
from flask import Flask, request, redirect, url_for, abort, send_from_directory, session, Response
from flask import render_template
from werkzeug.utils import secure_filename
import sys
import os
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import pymysql
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from pylab import title, figure, xlabel, ylabel, xticks, bar, legend, axis, savefig
from fpdf import FPDF
sys.stdout.encoding


sys.path.insert(1, './potholesx')
from predict import _main_


ROOT_DIR = os.path.abspath("./uploads")

UPLOAD_FOLDER = 'uploads'

app = Flask(__name__)

app.debug = True
app.secret_key = 'your secret key'

# Enter your database connection details below
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'timothy'
app.config['MYSQL_PASSWORD'] = 'mickeygerman1'
app.config['MYSQL_DB'] = 'Finalyear'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Intialize MySQL
mysql = MySQL(app)


@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/Home')
def home_page():
    if 'loggedin' in session:
        return render_template('Home.html', username=session['username'],role=session['role'])

    return redirect(url_for('index_page'))


@app.route('/traffic-analysis')
def traffic_analysis():
    if 'loggedin' in session:
        return render_template('TrafficAnalysis.html', username=session['username'],role=session['role'])

    return redirect(url_for('index_page'))


@app.route('/pothole-detection')
def pothole_detection():
    if 'loggedin' in session:
        files = os.listdir(ROOT_DIR)
        return render_template('PotHoleDetection.html', username=session['username'], files=files,role=session['role'])

    return redirect(url_for('index_page'))


@app.route('/reports')
def reports_page():
    if 'loggedin' in session:
        return render_template('reports.html', username=session['username'],role=session['role'])

    return redirect(url_for('index_page'))


@app.route('/email')
def email_page():
    if 'loggedin' in session:
        return render_template('Email.html', username=session['username'],role=session['role'])

    return redirect(url_for('index_page'))


@app.route('/sendemail')
def send_Email():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT Email FROM Users WHERE Role = 1 ')

    for x in cursor.fetchall():
        sendEmail(x)
    return render_template('Email.html')


@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    # Redirect to login page
    return redirect(url_for('index_page'))


# backend routes


@app.route('/upload')
def upload():
    files = os.listdir(ROOT_DIR)
    return render_template('upload.html', files=files)


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        area = request.form['Area']
        paved = request.form['Paved']
        traffic = request.form['Traffic']
        traffic_flow = request.form['Traffic-flow']
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save('uploads/'+secure_filename(f.filename))
        new_path = os.path.join(ROOT_DIR, filename)
        print(new_path)
        potholes = _main_(new_path)
        pothole_message = 'No potholes Detected'
        if potholes >= 1:
            pothole_message = 'Potholes Detected'

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        cursor.execute('INSERT INTO RoadDetails (Area,Paved,Traffic,Traffic_Flow,Pothole) VALUES (%s, %s,%s, %s, %s)',
                       (area, paved, traffic, traffic_flow, pothole_message,))
        mysql.connection.commit()
        msg = 'Details submitted successfully !'

        return render_template('PotHoleDetection.html', message=msg)
    elif request.method == 'POST':
        msg = 'Please fill out the form!'
        return render_template('PotHoleDetection.html', message=msg)


@app.route('/uploads/<filename>')
def viewFiles(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/login', methods=['GET', 'POST'])
def login():

    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'SELECT * FROM Users WHERE Username = %s AND Password = %s', (username, password,))

        account = cursor.fetchone()

        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account['ID']
            session['username'] = account['Username']
            session['role'] = account['Role']
            # Redirect to home page
            return redirect(url_for('home_page',username=session['username']))

            # return render_template('Home.html', username=session['username'])
        else:

            msg = 'Incorrect username/password!'

     # Show the login form with message (if any)
    return render_template('index.html', msg=msg)


@app.route('/register', methods=['GET', 'POST'])
def register():

    msg = ''

    if 'loggedin' not in session:
        return render_template('index.html', msg=msg)

    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access

        firstname = request.form['firstname']
        lastname = request.form['lastname']
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        role = request.form['Role']

        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM Users WHERE username = %s', (username,))
        account = cursor.fetchone()
        # If account exists show error and validation checks
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            cursor.execute('INSERT INTO Users (Firstname,Lastname,Username,Email,Password,Role) VALUES (%s, %s,%s, %s, %s, %s)',
                           (firstname, lastname, username,email, password, role))
            mysql.connection.commit()
            msg = 'You have successfully registered!'

            sendPassword(email,password)
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('register.html', msg=msg,username=session['username'],role=session['role'])


# generating report
@app.route('/download/report/pdf')
def download_report():

    
    # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    # sizes = []

    # cursor.execute("SELECT COUNT(*) AS count FROM RoadDetails WHERE Paved = 'Gravel'")
    # result_gravel = cursor.fetchall()
    # gravel=result_gravel[0]['count']
    # sizes.append(gravel)
    # cursor.execute("SELECT COUNT(*) AS count FROM RoadDetails WHERE Paved = 'Earth'")
    # result_earth = cursor.fetchall()
    # earth=result_earth[0]['count']

    # sizes.append(earth)

    
    # # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    # labels =  'Gravel','Earth'
    
    # explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

    # fig1, ax1 = plt.subplots()
    # ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
    #         shadow=True, startangle=90)
    # ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # savefig('piechart.png')




    pdf = FPDF()
    try:

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        cursor.execute(
            "SELECT Area, Paved, Traffic, Traffic_Flow,Pothole FROM RoadDetails")
        result = cursor.fetchall()

        pdf.add_page()

        page_width = pdf.w - 2 * pdf.l_margin

        pdf.set_font('Times', 'B', 14.0)
        pdf.set_text_color(255,0,0)
        pdf.cell(page_width, 0.0, 'Kampala City Council Authority Road Report', align='C')
        pdf.ln(5)
        pdf.set_font('Courier', '', 10)
        pdf.cell(page_width, 0.0, 'For A Better City', align='C')
        pdf.ln(10)

        pdf.set_text_color(0,0,0)
        col_width = page_width/5

        pdf.ln(1)

        th = pdf.font_size
        pdf.cell(col_width, th, 'Area', border=1)
        pdf.cell(col_width, th, 'Paved', border=1)
        pdf.cell(col_width, th, 'Traffic', border=1)
        pdf.cell(col_width, th, 'Traffic_Flow', border=1)
        pdf.cell(col_width, th, 'Pothole', border=1)
        pdf.ln(th)

        for row in result:
            pdf.cell(col_width, th, row['Area'], border=1)
            pdf.cell(col_width, th, row['Paved'], border=1)
            pdf.cell(col_width, th, row['Traffic'], border=1)
            pdf.cell(col_width, th, row['Traffic_Flow'], border=1)
            pdf.cell(col_width, th, row['Pothole'], border=1)
            pdf.ln(th)
        
        pdf.ln(5)

        pdf.write(5, 'Piechart showing classification  of Roads in % ')
        pdf.ln(5)

        pdf.image('piechart.png', x = None, y = None, w = 100, h = 100, type = '', link = '')

        
        pdf.write(5, 'Areas that are both Gravel and with potholes  :')
        pdf.ln(5)
        

        for row in result:
            if row['Pothole']=='Potholes Detected' and row['Paved']=='Gravel' :
                pdf.write(5, '%s'%(row['Area']) )
                pdf.ln(5)

        pdf.write(5, 'Areas that are both Earth and with potholes  :')
        pdf.ln(5)

        for row in result:
            if row['Pothole']=='Potholes Detected' and row['Paved']=='Earth' :
                pdf.write(5, '%s'%(row['Area']) )
                pdf.ln(5)
            

        pdf.write(5, 'Areas with High Traffic, Earth and potholes  :')
        pdf.ln(5)

        for row in result:
            if row['Pothole']=='Potholes Detected' and row['Paved']=='Earth' and row['Traffic']=='High' :
                pdf.write(5, '%s'%(row['Area']) )
                pdf.ln(5)
            
                


        

        pdf.ln(10)

        pdf.set_font('Times', '', 10.0)
        pdf.cell(page_width, 0.0, '- end of report -', align='C')
        pdf.output('Reports/Report.pdf', 'F')

    except Exception as e:
        print(e)
    finally:
        return Response(pdf.output(name='timo', dest='S'), mimetype='application/pdf', headers={'Content-Disposition': 'attachment;filename=Report.pdf'})
