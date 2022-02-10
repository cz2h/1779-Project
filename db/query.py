def get_filename_query(table, key):
    return f'SELECT file_name FROM {table} WHERE  file_key=\'{key}\''
