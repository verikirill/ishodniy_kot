import os

from flask import Flask, render_template, redirect, request, abort, jsonify

UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chipinkpos'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(port=8082, host='127.0.0.1', debug=True, use_reloader=True)
