from flask import Flask, render_template,request
from werkzeug.utils import secure_filename
from pathlib import Path
import os.path
app = Flask(__name__, template_folder='template')

# global file;

@app.route("/")
def home():
	return render_template('home.html')
    # return "This is the home page, ok"

@app.route('/clicked')
def clicked():
	return 'clicked'

@app.route('/uploader',methods=['POST'])
def upload_file():
    if request.method == 'POST':

    	# there is no key by the name of 'file'
    	# works ok with text inputs but not file

    	# f = request.form
    	# if "file" in f:
    	# 	print ('yes')
    	# filename=f['file']


    	# cannot find the path from this because the object retured is of type file storage and to use os.path or Path we need string 
    	# this returns file storage object
    	f=request.files['file']
    	# this save the file in the desired/default folder
    	# f.save(secure_filename(f.filename))
    	#find the filename
    	file=secure_filename(f.filename)
    	return "file sent successfully"

    	# filename=os.path.join(filename)
    # if filename.exists():
    # 	return "file sent successfully"
    return 'file not sent'
    
if __name__ == "__main__":
    app.run(debug=True)