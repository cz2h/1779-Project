def post_table_query():
    return 'create table file_names (  file_key  VARCHAR(32) not null, file_name VARCHAR(32) null,    constraint ' \
           'file_names_pk        primary key (file_key)); '


def get_filename_query(table, key):
    return f'SELECT file_name FROM {table} WHERE  file_key=\'{key}\';'


def get_all_file_key_query(table):
    return f'SELECT file_key FROM {table};'


def post_file_key_and_name(table, file_key, file_name):
    return f'INSERT INTO {table} VALUE (\'{file_key}\', \'{file_name}\') ' \
           f'ON DUPLICATE KEY UPDATE file_name=\'{file_name}\';'
