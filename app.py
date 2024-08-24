import os

from flask import Flask, request, render_template
from flask import send_from_directory
from werkzeug.utils import secure_filename

from SaintScript.ascii_converter import img_to_ascii
from SaintScript.resizer import img_resize
from api import create_api

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Max upload size is 16MB

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])


@app.route('/')
def index():
    print("getting index")
    return render_template('classic.html')


@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)


@app.route('/', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        screen_width = int(request.form['screen_width'])
        screen_height = int(request.form['screen_height'])
        print(f'Screen width: {screen_width}, Screen height: {screen_height}')

        # # Resize the image to fit the screen dimensions while maintaining aspect ratio
        # with Image.open(file_path) as img:
        #     img_ratio = img.width / img.height
        #     screen_ratio = screen_width / screen_height
        #
        #     if img_ratio > screen_ratio:
        #         new_width = screen_width
        #         new_height = int(new_width / img_ratio)
        #     else:
        #         new_height = screen_height
        #         new_width = int(new_height * img_ratio)
        #
        #     img = img.resize((new_width, new_height), Image.ANTIALIAS)
        #     img.save(file_path)

        img_resize(file_path, int(screen_width / 5.0), int(screen_height / 5.0))

        ascii_art = img_to_ascii(file_path)
        os.remove(file_path)  # Optionally delete the file after processing
        return ascii_art


create_api(app)

if __name__ == '__main__':
    app.run(debug=True)
