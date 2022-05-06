import os, uuid
import yaml
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__,ContentSettings
import random

# Retrieve the connection string for use with the application. The storage
# connection string is stored in an environment variable on the machine
# running the application called AZURE_STORAGE_CONNECTION_STRING. If the environment variable is
# created after the application is launched in a console or with Visual Studio,
# the shell or application needs to be closed and reloaded to take the
# environment variable into account.d
connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING') 
try:
    
    print("Azure Blob Storage v" + __version__ + " - Python quickstart sample")

    # Quick start code goes here

except Exception as ex:
    print('Exception:')
    print(ex)
 
# Create the BlobServiceClient object which will be used to create a container client
blob_service_client = BlobServiceClient.from_connection_string(connect_str)
def get_random_string(length):
    # choose from all lowercase letter
    letters = 'YZ1fghijkAMl56ijkAMl56e9rste9rstum234vwxBQpqrstumCDE0yzNOPnR78aboVWXQpqFGHIJKLcdSTU'
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
# Instantiates a client
#storage_client = storage.Client()
# Create a unique name for the container
def get_random_container(length):
    # choose from all lowercase letter
    letters = 'lmnojkuiqrsitefgaiycvwxpz'
    container_name  = ''.join(random.choice(letters) for i in range(length))
    return container_name 
for i in range(0,1):
        # The name for the new bucket
        ra = get_random_string(random.randint(30,40))
        bucket_name = ra.lower()
        #print(bucket_name)
        # Create the container
        container_client = blob_service_client.create_container(bucket_name,public_access='container')  
        #bucket detail
        #vars(bucket)

        #accessing a Specific Bucket

        my_bucket = container_client.get_container_properties()
def load_config():
    dir_root=os.path.dirname(os.path.abspath(__file__))
    with open(dir_root +"C:/Users/fouda/OneDrive/Bureau/FOUDA/blob-quickstart-v12/","r") as yamlfile:
         return yaml.load(yamlfile, Loader=yaml.FullLoader)
def get_files(dir):
    with os.scandir(dir) as entries:
         for entry in entries:
             if entry.is_file() and not entry.name.startswith('.'):
                 yield entry
#upload files
def upload(files, connection_string, container_name):
    container_client=ContainerClient.from_connection_string(connection_string, my_bucket)
    print("Uploading files to blob storage...")

    for file in files:
        blob_client=container_client.get_blob_client(file.name)
        with open(file.path,"rb") as data:
             blob_client.upload_blob(data)
             print(f'{file.path} uploaded to blob storage')
             os.remove(file)
             print(f'{file.name} removed from folder')
        
config = load_config()
videos= get_files(config["source_folder"]+"img")
upload(videos, config["azure_storage_connectionstring"], config["videos_container_name"])
