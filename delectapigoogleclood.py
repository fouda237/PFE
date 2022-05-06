from itertools import count
import os
import string
import random
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS']='ServiceKey_GoogleCloud.json'
bucket_name="004fdndr1g2xcigxx0ulgfdrqvxle5eex5rb"
directory_name = ''
client=storage.Client()
bucket = client.get_bucket(bucket_name)
print(* bucket_name)
# list all objects in the directory
blob_list = bucket.list_blobs()
print(* blob_list)
a=[]
for blob in blob_list:
    a.append(blob.name)
fileCount=len(a)
if fileCount==0:
    bucket.delete()
    print("{} has been deleted successfully !!!".format(bucket_name)) 
else:
    print("{} is not empty {} objects present".format(bucket_name,fileCount))
    print("Please make sure S3 bucket is empty before deleting it !!!")
    blob_list = bucket.list_blobs()
    for blob in blob_list:   
        blob.delete()
    bucket.delete()      
    print("{} has been deleted successfully !!!".format(bucket_name)) 

