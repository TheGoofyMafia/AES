from flask import Flask, render_template, request
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


@app.route('/uploader', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save((f.filename))
        file = (f.filename)
        print(file)
        return "file sent successfully"
    return 'file not sent'


if __name__ == "__main__":
    app.run(debug=True)
