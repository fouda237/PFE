import os
import random
import shutil
import boto3
import json

orl=r'C:\Users\fouda\OneDrive\Bureau\yandex cloud\filles\hada.html'
def get_random_string_lowercas(length):
    # choose from all lowercase letter
    letters = 'ichuvwxatjelysopkfgmndqrbz'
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def get_random_string(length):
    # choose from all lowercase letter
    letters = 'xR0nopWXYvZ1de9NOPFGhyLMSTHsK34aQjkliqrDEfgCzAB2bcUV67w58m'
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
# session = boto3.session.Session()
s3 = boto3.client(
    service_name='s3',
    aws_access_key_id='YCAJEmzKcuiw6mpoh_OXM_0Ig',
    aws_secret_access_key='YCO0K-OrfwEQGhHC8CXD3u-vjBIPVH1JhGTWmTWu',
    endpoint_url='https://storage.yandexcloud.net'
)
for i in range(0,1):
        # The nam for the new bucket
        ra = get_random_string(random.randint(30,40))
        bucket_name = ra.lower()
        # Creating a new bucket
        bucket=s3.create_bucket(Bucket=bucket_name,ACL='public-read-write')
        
        # result=s3.get_bucket_acl(Bucket=bucket_name)
        # print(result)
        for i in range(1):
              b=get_random_string_lowercas(30)
              # print(b)
              orli="C:/Users/fouda/OneDrive/Bureau/yandex cloud/hadalLinks/"+b+".html"
              shutil.copyfile(orl, orli)
              l="https://storage.yandexcloud.net/"+bucket_name+"/"+b+".html"
              links=open('linkshtml.txt','a')
              links.write(l+'\n')
              links.close()
