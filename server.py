import os

from flask import Flask, render_template, redirect, request, abort, jsonify

UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chipinkpos'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'save' in request.form:
            print(request.form)
    return render_template('index.html')


@app.route('/get-data', methods=['POST'])
def get_data():
    data = request.get_json()
    content = data.get('content')
    print(f'Полученные данные: {content}')
    return jsonify({"status": "success", "received_content": content})


if __name__ == '__main__':
    app.run(port=8082, host='127.0.0.1', debug=True, use_reloader=True)