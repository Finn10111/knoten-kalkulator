from flask import jsonify, request
import os
import uuid
from . import api
from .. import io
from .. import db
from flask_login import login_required
from flask_jwt_extended import jwt_required
from werkzeug.utils import secure_filename

@api.route('/images/upload', methods=['POST'])
def image_upload():
    # check if the post request has the file part
    if 'file' not in request.files:
        return False
    file = request.files['file']
    # if user does not select file, browser also
    # submit a empty part without filename
    if file.filename == '':
        return False
    if file and allowed_file(file.filename):
        #filename = secure_filename(file.filename)
        filename = str(uuid.uuid4()) + '.' + file.filename.rsplit('.', 1)[1].lower()
        file.save(os.path.join(os.path.dirname(os.path.realpath(__file__))+'/../../static/img', filename))
        return ({'filename': filename})
    return jsonify(False)

def allowed_file(filename):
   ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
   return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

