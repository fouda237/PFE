import os
import random
import shutil
import boto3
import json
s3 = boto3.client(
    service_name='s3',
    aws_access_key_id='YCAJEmzKcuiw6mpoh_OXM_0Ig',
    aws_secret_access_key='YCO0K-OrfwEQGhHC8CXD3u-vjBIPVH1JhGTWmTWu',
    endpoint_url='https://storage.yandexcloud.net'
)
bucket_name="fou"
bucket=s3.create_bucket(Bucket=bucket_name,ACL='public-read-write')