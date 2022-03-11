from extensions import s3


def save_file_to_s3(key, file, bucket_name='1779test'):
    s3.put_object(Bucket=bucket_name, Key=key, Body=file)


def get_file_from_s3(key, bucket_name='1779test'):
    response = s3.get_object(Bucket=bucket_name, Key=key)
    return response['Body']
