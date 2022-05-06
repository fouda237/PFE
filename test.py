import os
import string
import random
from google.cloud import storage
os.environ['GOOGLE_APPLICATION_CREDENTIALS']='ServiceKey_GoogleCloud.json'
storage_client=storage.Client()
bucket_name='004fdndr1g2xcigxx0ulgfdrqvxle5eex5rb'
# a=storage_client.bucket(bucket_name)
# print(a)
bucket=storage_client.list_buckets()
# for b in bucket:
#     h=b.name
#     links=open('listeBucket.txt','a')  
#     links.write(h +'\n')  
#     links.close()
# pro=storage_client.list_buckets(creation="04/2022")
# print(* pro)
# p=storage_client.get_bucket(creation="17 avril 2022")
# print(p)
# a=dir(storage_client)
# print(a)
if bucket_name in bucket:
    print('exist')
else:
    print("n'exist pas")    