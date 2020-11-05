from flask import Flask,request,redirect, url_for,abort,send_from_directory
from flask import render_template
from werkzeug.utils import secure_filename
import sys
import os
sys.path.insert(1, './potholesx')
from predict import _main_

ROOT_DIR = os.path.abspath("./uploads")

UPLOAD_FOLDER = 'uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def hello_world():
    return 'hey you dashboard'

@app.route('/traffic')
def hello():
    return render_template('placesApi/placeAutoComplete.html')

@app.route('/upload')
def upload():
    files = os.listdir(ROOT_DIR)
    return render_template('upload.html', files=files)
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      filename = secure_filename(f.filename)
      f.save('uploads/'+secure_filename(f.filename))
      new_path = os.path.join(ROOT_DIR, filename)
      print(new_path)
      potholes= _main_(new_path)
    #   return  'Hey {} pothole(s) been detected!'.format(str (potholes))
      return redirect(url_for('upload'))



@app.route('/uploads/<filename>')
def viewFiles(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

