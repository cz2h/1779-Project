from flask import Blueprint, request, current_app

from db import db_access

from models.error import Error
from models.reply import Reply

cachepool_route_blueprint = Blueprint('cachepool_route', __name__, url_prefix='/api/pool')


@cachepool_route_blueprint('/resize', methods=['POST'])
def post_resize():
    # TODO: Implement this api. Want to re-initiate HashRouter
    return Reply(success=False).to_json()