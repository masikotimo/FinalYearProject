from flask import Flask,request
from flask import render_template
from werkzeug.utils import secure_filename
import sys
import os
sys.path.insert(1, './potholesx')
from predict import _main_


UPLOAD_FOLDER = '/uploads'

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
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      filename = secure_filename(f.filename)
      f.save(secure_filename(f.filename))
      new_path = os.path.abspath(filename)
      potholes= _main_(new_path)
    #   f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))


      return  'Hey {} pothole(s) been detected!'.format(str (potholes))