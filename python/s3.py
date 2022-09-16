
import logging
import boto3
from botocore.exceptions import ClientError
import os
from boto3.session import Session
session = Session(aws_access_key_id='AWS_ACCESS_KEY_ID', aws_secret_access_key='AWS_SECRET_ACCESS_KEY', region_name='region_name')

#获取s3连接的session
s3 = session.resource('s3')
for bucket in s3.buckets.all():
    print('bucket name:%s'%bucket.name)

object_name = os.path.basename('C:/Users/TibeMe_user/Desktop/s3.txt')
# print(object_name)

os.environ['AWS_ACCESS_KEY_ID'] = "AWS_ACCESS_KEY_ID"
os.environ['AWS_SECRET_ACCESS_KEY'] = "AWS_SECRET_ACCESS_KEY"


def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(s3.txt)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True




upload_file("C:/Users/TibeMe_user/Desktop/s3.txt", "tests3buckettt", '1234')