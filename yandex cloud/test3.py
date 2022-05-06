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
## From a string
# s3.put_object(Bucket='fou', Key='object_name', Body='TEST', StorageClass='COLD')
## From a file
s3.upload_file('C:/Users/fouda/OneDrive/Bureau/yandex cloud/filles/hada.png', 'fou', 'py_script.png')
# s3.upload_file('this_script.py', 'bucket-name', 'script/py_script.py')