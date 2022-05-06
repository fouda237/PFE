from itertools import count
import os
import string
import random
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS']='ServiceKey_GoogleCloud.json'
# bucket_name="004fdndr1g2xcigxx0ulgfdrqvxle5eex5rb"
list_bucket=[]
client=storage.Client()
with open('C:/Users/fouda/OneDrive/Bureau/api google cloud/test.txt','r') as  fichier :
     for bucket_name in fichier :
         list_bucket.append(bucket_name)
for name_bucket in list_bucket:
    str=name_bucket.replace('\n',"")
    # bucket=client.get_bucket(str)
    bucket=client.list_buckets()
    if str in bucket:
        print("exist")
        #  list all objects in the directory
        blob_list=bucket.list_blobs()
        # print(* blob_list)
        a=[]
        for blob in blob_list:
            a.append(blob.name)
        fileCount=len(a)
        if fileCount==0:
            bucket.delete()
            print("{} has been deleted successfully !!!".format(str)) 
        else:
            print("{} is not empty {} objects present".format(str,fileCount))
            print("Please make sure S3 bucket is empty before deleting it !!!")
            blob_list = bucket.list_blobs()
            for blob in blob_list:   
                blob.delete()
            bucket.delete()      
            print("{} has been deleted successfully !!!".format(bucket_name)) 
    else:
        print("n'existe pas")

 

