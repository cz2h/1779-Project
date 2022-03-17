from flask import Blueprint, request, current_app

from models.error import Error
from models.reply import Reply

manager_blueprint = Blueprint('manager_route', __name__, url_prefix='/api/manager')


@manager_blueprint.route('/clear', methods=['POST'])
def post_clear_files():
    # TODO: Clear all files
    return Reply(success=True).to_json()
