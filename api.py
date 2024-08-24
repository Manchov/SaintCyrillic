import os

from flask import request
from flask_restful import Api, Resource
from werkzeug.utils import secure_filename

from SaintScript.ascii_converter import img_to_ascii
from SaintScript.resizer import img_resize

UPLOAD_FOLDER = 'uploads'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


class AsciiArtAPI(Resource):
    def post(self):
        if 'file' not in request.files:
            return {'message': 'No file part'}, 400
        file = request.files['file']
        if file.filename == '':
            return {'message': 'No selected file'}, 400
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(file_path)

            screen_width = request.form.get('screen_width', type=float)
            screen_height = request.form.get('screen_height', type=float)

            img_resize(file_path, int(screen_width / 5.0), int(screen_height / 5.0))

            ascii_art = img_to_ascii(file_path, type="cyrillic")
            os.remove(file_path)  # Optionally delete the file after processing
            return {'ascii_art': ascii_art}


def create_api(app):
    api = Api(app)
    api.add_resource(AsciiArtAPI, '/api/ascii-art')
    return api
