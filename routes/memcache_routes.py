from flask import Blueprint

from models.reply import Reply

from db.db_access import get_memcache_stat as db_get_cache_stat
memcache_blueprint = Blueprint('memcache_route', __name__, url_prefix='/api/memcache')


@memcache_blueprint.route('/stat', methods=['GET'])
def get_memcache_stat():
    stats = db_get_cache_stat()
    print(stats)
    if stats is not None or len(stats) > 0:
        return Reply(success=True, stat=stats).to_json()
    return Reply(success=False).to_json()
