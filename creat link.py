import os
import string
import random
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS']='ServiceKey_GoogleCloud.json'


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
# Instantiates a client
storage_client = storage.Client()

##### numbre bucket
for i in range(0,1):
        # The nam for the new bucket
        ra = get_random_string(random.randint(30,40))
        bucket_name = ra.lower()
        print(bucket_name)


        #print(dir(storage_client))

        bucket = storage_client.create_bucket(bucket_name)


        #bucket detail
        #vars(bucket)

        #accessing a Specific Bucket

        my_bucket = storage_client.get_bucket(bucket_name)

        #upload files

        def upload_blob(bucket_name, source_file_name, destination_blob_name):
            """Uploads a file to the bucket."""
            # bucket_name = "your-bucket-name"
            # source_file_name = "local/path/to/file"
            # destination_blob_name = "storage-object-name"

            storage_client = storage.Client()
            bucket = storage_client.bucket(bucket_name)
            blob = bucket.blob(destination_blob_name)

            blob.upload_from_filename(source_file_name)

            #print("File {} uploaded to {}.".format(source_file_name, destination_blob_name))
##### numbre suffix
        for b in range(0,1) :
                    file_path=r'C:\Users\fouda\OneDrive\Bureau\api google cloud\filles'
                    filename=get_random_string_lowercas(random.randint(30,40))
                    upload_blob(bucket_name,os.path.join(file_path,'hada.html'),filename)

                    #upload_blob(bucket_name,os.path.join(file_path,'hada.html'),filename)



                    def view_bucket_iam_members(bucket_name):
                        """View IAM Policy for a bucket"""
                        # bucket_name = "your-bucket-name"

                        storage_client = storage.Client()
                        bucket = storage_client.bucket(bucket_name)

                        policy = bucket.get_iam_policy(requested_policy_version=3)

                        #for binding in policy.bindings:
                            #print("Role: {}, Members: {}".format(binding["role"], binding["members"]))


                    view_bucket_iam_members(bucket_name)


                    def add_bucket_iam_member(bucket_name, role, member):
                        """Add a new member to an IAM Policy"""
                        # bucket_name = "your-bucket-name"
                        # role = "IAM role, e.g. roles/storage.objectViewer"
                        # member = "IAM identity, e.g. user: name@example.com"

                        storage_client = storage.Client()
                        bucket = storage_client.bucket(bucket_name)

                        policy = bucket.get_iam_policy(requested_policy_version=3)

                        policy.bindings.append({"role": role, "members": {member}})

                        bucket.set_iam_policy(policy)

                        #print("Added {} with role {} to {}.".format(member, role, bucket_name))

                    role='roles/storage.legacyObjectReader'
                    member='allUsers'

                    add_bucket_iam_member(bucket_name, role, member)



                    #getting links


                    links=open('AllLinks.txt','a')

                    l='https://'+ra+'.storage.googleapis.com/'+filename
                    links.write(l+'\n')
                    links.close()
print('complete')
