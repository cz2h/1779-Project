from flask import Blueprint, request, current_app
from models.reply import Reply

from util.string_processor import get_sha256

from db.db_access import get_filename_by_key

import base64
import logging
import os

logger = logging.getLogger(__name__)

file_blueprint = Blueprint('file_route', __name__, url_prefix='/api')


@file_blueprint.route('/test')
def get_test():
    data = get_filename_by_key('k1')
    return {
        "status": "Who?",
        "data": data
    }


@file_blueprint.route('/upload', methods=['POST'])
def post_file():
    key = str(request.form.get('key'))

    # TODO: DB replace key if necessary

    file = request.files['file']
    if file:
        filename = get_sha256(key) + file.filename
        file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        return Reply(success=True).to_json()
    else:
        return Reply(success=False).to_json()


@file_blueprint.route('/key/', methods=['POST'])
def get_file():
    key = str(request.args.get('key_value'))

    # TODO: Get the file name through DB
    filename = 'e51.jpeg'
    target_filename = get_sha256(key) + filename
    with open(os.path.join(current_app.config['UPLOAD_FOLDER'], target_filename), 'rb') as binary_file:
        binary_data = binary_file.read()
        base64_data = base64.b64encode(binary_data)
        base64_msg = base64_data.decode('utf-8')
    return Reply(success=True, content=base64_msg).to_json()


def get_all_keys():
    return Reply(success=True, keys=[]).to_json()
