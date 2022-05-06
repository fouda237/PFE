import os
import random
import shutil
import boto3
import json
client = boto3.client(
    's3',
    aws_access_key_id='AKIA2VJ3JGY2WVF5YROF',
    aws_secret_access_key='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'
    # aws_session_token=SESSION_TOKEN
)
bucket_name=str(input('Please input bucket name to be deleted: '))
print("Before deleting the bucket we need to check if its empty. Cheking ...")
objects = client.list_objects_v2(Bucket=bucket_name)
fileCount = objects['KeyCount']

if fileCount == 0:
 response = client.delete_bucket(Bucket=bucket_name)
 print("{} has been deleted successfully !!!".format(bucket_name))
else:
 print("{} is not empty {} objects present".format(bucket_name,fileCount))
 print("Please make sure S3 bucket is empty before deleting it !!!")
 for key in client.list_objects(Bucket=bucket_name)['Contents']:
     p=key['Key']
     if p==0:
         print("bucket vide")
     else:    
        client.delete_object(Bucket=bucket_name, Key=p)
        print("fichier effacé")
 response = client.delete_bucket(Bucket=bucket_name) 
 print("{} has been deleted successfully !!!".format(bucket_name))      
