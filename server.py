from flask import Flask, redirect, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
	if request.method == 'POST':
		f = request.files['file']
		f.save(os.path.join(os.path.dirname(__file__), '',secure_filename(f.filename)))
		return redirect('/')
	return '<!DOCTYPE html><html><head></head><body><form action="" method="POST" enctype="multipart/form-data"><input type="file" name="file"><input type="submit" value="Upload"></form></body></html>'

app.run(host='0.0.0.0',port=3001)