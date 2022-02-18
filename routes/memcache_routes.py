from flask import Blueprint, request

from models.reply import Reply

from db.db_access import get_memcache_stat as db_get_cache_stat, post_memcache_config as db_post_cache_config
memcache_blueprint = Blueprint('memcache_route', __name__, url_prefix='/api/memcache')


@memcache_blueprint.route('/stat', methods=['GET'])
def get_memcache_stat():
    stats = db_get_cache_stat()
    if stats is not None or len(stats) > 0:
        return Reply(success=True, stat=stats).to_json()
    return Reply(success=False).to_json()


@memcache_blueprint.route('/set', methods=['POST'])
def post_memcache_config():
    capacity = request.form.get('capacity')
    rep_policy = request.form.get('rep_policy')
    print(capacity, rep_policy)
    if db_post_cache_config(capacity, rep_policy):
        return Reply(success=True).to_json()
    return Reply(success=False).to_json()
