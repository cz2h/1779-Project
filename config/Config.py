import os


class DevConfig(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    UPLOAD_FOLDER = './image_library'
    ALLOWED_FORMAT = {'jpg', 'jpeg', 'png', 'gif', 'tiff'}
    FILENAME_SEPARATOR = '_'
    DB_CONFIG = {
        'user': '',
        'password': '',
        'host': 'localhost',
        'database': 'Assignment_1',
        'table': 'keylist',
        'memcache_stat_table': 'cache_stats',
        'memcache_config_table': 'memcache_config'
    }
    # TODO: Provide your local login info.
    MYSQL_DATABASE_USER = ''
    MYSQL_DATABASE_PASSWORD = ''
    MYSQL_DATABASE_DB = 'Assignment_1'
    MYSQL_DATABASE_HOST = 'localhost'
    # Memcache related macro
    MEMCACHE_SERVER = 'http://192.168.2.104:5001'
    END_POINTS = {
        'put': '/put',
        'get': '/get',
        'clear': '/clear',
        'invalidatekey': '/invalidatekey',
        'refreshconfiguration': '/refreshconfiguration'
    }
