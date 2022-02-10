import extensions
from config.Config import DevConfig

from db.query import get_filename_query


def get_filename_by_key(key):
    cnx = extensions.mysql.connect()
    cursor = cnx.cursor()
    query = get_filename_query(DevConfig.DB_CONFIG['table'], key)
    cursor.execute(query)
    row = cursor.fetchone()
    if row is None:
        print('Not found')
        return None
    else:
        return row[0]