from flask import Blueprint, request, current_app

from models.error import Error
from models.reply import Reply

from util.string_processor import get_sha256

from db.db_access import get_filename_by_key, post_key_filename, get_all_file_keys

import base64
import logging
import os

logger = logging.getLogger(__name__)

file_blueprint = Blueprint('file_route', __name__, url_prefix='/api')


@file_blueprint.route('/test')
def get_test():
    data = post_key_filename('k1', 'is not mma.jpg')
    return {
        "status": "Who?",
        "data": data
    }


@file_blueprint.route('/upload', methods=['POST'])
def post_file():
    key = str(request.form.get('key'))
    file = request.files['file']
    if file:
        if not post_key_filename(key, file.filename):
            return Reply(success=False, error=Error(500, "Fail to update DB"))
        filename = get_sha256(key) + file.filename
        file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        return Reply(success=True).to_json()
    else:
        return Reply(success=False).to_json()


@file_blueprint.route('/key/', methods=['POST'])
def get_file():
    key = request.args.get('key')
    if key is None:
        return Reply(success=False, error=Error(400, "No param key is given")).to_json()
    key = str(key)
    filename = get_filename_by_key(key)
    if filename is None:
        return Reply(success=False, error=Error(204, "No such file available")).to_json()
    target_filename = get_sha256(key) + filename
    with open(os.path.join(current_app.config['UPLOAD_FOLDER'], target_filename), 'rb') as binary_file:
        binary_data = binary_file.read()
        base64_data = base64.b64encode(binary_data)
        base64_msg = base64_data.decode('utf-8')
    return Reply(success=True, content=base64_msg).to_json()


@file_blueprint.route('/list_keys', methods=['POST'])
def get_all_keys():
    all_keys = get_all_file_keys()
    if all_keys is None:
        return Reply(success=False, error=Error(500, "Failed to execute query")).to_json()
    return Reply(success=True, keys=all_keys).to_json()
