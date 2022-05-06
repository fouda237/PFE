import os
import random
import shutil
import boto3
import json

orl=r'C:\Users\fouda\OneDrive\Bureau\yandex\hada.html'
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
client = boto3.client(
    's3',
    aws_access_key_id='AKIA2VJ3JGY2WVF5YROF',
    aws_secret_access_key='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'
    # aws_session_token=SESSION_TOKEN
)
##### numbre bucket
for i in range(0,1):
        # The nam for the new bucket
        ra = get_random_string(random.randint(30,40))
        bucket_name = ra.lower()
        # print(bucket_name)
        location='us-west-2'
        # 'af-south-1' | ' ap-est-1' | 'ap-nord-est-1' | 'ap-nord-est-2' | 'ap-nord-est-3' | 'ap-sud-1' | 'ap-sud-est-1' | ' ap-sud-est-2' | 'ca-central-1' |'cn-nord-1' | 'cn-nord-ouest-1' | 'UE' | 'eu-central-1' | 'eu-nord-1' | 'eu-sud-1' | 'eu-west-1' | 'eu-west-2' | 'eu-ouest-3' | 'moi-sud-1' | 'sa-est-1' | 'us-east-2' | 'us-gov-east-1' | 'us-gov-west-1' | 'us-west-1' | 'us-west-2' 
    
          # Create bucket
        reponse=client.create_bucket (ACL='public-read-write',Bucket=bucket_name,CreateBucketConfiguration={'LocationConstraint':location})
        #,ObjectLockEnabledForBucket=False ,ObjectOwnership='BucketOwnerEnforced' BucketOwnerPreferred| 'ObjectWriter' | ''), GrantFullControl = 'string' ,GrantRead = 'string', GrantWrite = 'chaîne' ,GrantWriteACP = 'chaîne'       
        bucket_policy={
        "Version":"2012-10-17",
        "Statement":[
            {
                "Sid":"AddPerm",
                "Effect":"Allow",
                "Principal":"*",
                "Action":["s3:GetObject"],
                "Resource":["arn:aws:s3:::"+bucket_name+"/*"]
            }
         ]
        }
        policy_string=json.dumps(bucket_policy)
        client.put_bucket_policy(Bucket=bucket_name,Policy=policy_string)
        result=client.get_bucket_acl(Bucket=bucket_name)
        # a="kshanutfcturciytciyv"   
        for i in range(10):
              b=get_random_string_lowercas(30)
              # print(b)
              orli="C:/Users/fouda/OneDrive/Bureau/yandex/hadal/"+b+".html"
              shutil.copyfile(orl, orli)
              l="https://"+bucket_name+".s3."+location+".amazonaws.com/"+b+".html"
              links=open('links.txt','a')
              links.write(l+'\n')
              links.close()
