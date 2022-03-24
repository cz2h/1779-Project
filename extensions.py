from models.HashRouter import HashRouter
from flaskext.mysql import MySQL
import boto3

mysql = MySQL()

s3 = boto3.client('s3')

hash_router = HashRouter()
hash_router.init()