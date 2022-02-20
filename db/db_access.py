import datetime

import extensions
from config.Config import DevConfig

from db.query import get_filename_query, get_all_file_key_query, post_file_key_and_name, get_cache_stat, \
    post_update_cache_config, delete_cache_stat


def get_filename_by_key(key):
    try:
        cnx = extensions.mysql.connect()
        cursor = cnx.cursor()
        query = get_filename_query(DevConfig.DB_CONFIG['table'], key)
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            return None
        else:
            return row[0]
    except Exception:
        return None


def get_all_file_keys():
    try:
        cnx = extensions.mysql.connect()
        cursor = cnx.cursor()
        query = get_all_file_key_query(DevConfig.DB_CONFIG['table'])
        cursor.execute(query)
        nested_file_keys = cursor.fetchall()
        file_keys = [nested_file_keys[i][0] for i in range(len(nested_file_keys))]
        # In the form of [[k1], [k2]...]
        if file_keys is None:
            return None
        else:
            return file_keys
    except Exception:
        return None


def post_key_filename(file_key, file_name, file_size):
    try:
        cnx = extensions.mysql.connect()
        cursor = cnx.cursor()
        query = post_file_key_and_name(DevConfig.DB_CONFIG['table'], file_key, file_name, file_size)
        rows_affect = cursor.execute(query)
        cnx.commit()
        return True
    except Exception as err:
        return False


def get_memcache_stat():
    try:
        cnx = extensions.mysql.connect()
        cursor = cnx.cursor()
        query = get_cache_stat(DevConfig.DB_CONFIG['memcache_stat_table'], datetime.datetime.now() -
                               datetime.timedelta(minutes=10)
)
        print(query)
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows
    except Exception as err:
        print(err)
        return False


def post_memcache_config(capacity, rep_policy):
    try:
        cnx = extensions.mysql.connect()
        cursor = cnx.cursor()
        delete_query = delete_cache_stat(DevConfig.DB_CONFIG['memcache_config_table'])
        cursor.execute(delete_query)
        query = post_update_cache_config(DevConfig.DB_CONFIG['memcache_config_table'], capacity, rep_policy)
        cursor.execute(query)
        cnx.commit()
        return True
    except Exception:
        return False