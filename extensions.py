from flaskext.mysql import MySQL
import boto3

mysql = MySQL()

s3 = boto3.client('s3')
