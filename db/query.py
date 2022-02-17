def post_table_query():
    return 'create table file_names (  file_key  VARCHAR(32) not null, file_name VARCHAR(32) null,    constraint ' \
           'file_names_pk        primary key (file_key)); '


def get_filename_query(table, key):
    return f'SELECT filename FROM {table} WHERE  uniquekey=\'{key}\';'


def get_all_file_key_query(table):
    return f'SELECT uniquekey FROM {table};'


def post_file_key_and_name(table, file_key, file_name, file_size):
    print(file_size, file_name)
    return f"INSERT INTO {table} VALUE (\'{file_key}\', \'{file_name}\', \'{file_size}\')" + \
           'ON DUPLICATE KEY UPDATE filename=\'{name}\', '.format(name=file_name) + \
           f' image_size=\'{file_size}\';'
