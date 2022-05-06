import os
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__,ContentSettings
import random
import yaml

with open ("offre.yaml","r") as descript:
	fichier = yaml.safe_load(descript)

offer=fichier["offer"]

path="F:/test/offers/"+offer
key=fichier['key']
connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
def get_files(dir):
    with os.scandir(dir) as entries :
		                for entry in entries:
			                if entry.is_file() and not entry.name.startswith('.'):
			                   yield entry

def upload(files , connection_string , container_name):
	
	blob_service_client = BlobServiceClient.from_connection_string(connection_string)
	try : 
		container_client = blob_service_client.create_container(container_name,public_access='container' ) #creation
	except Exception as e:
		container_client = ContainerClient.from_connection_string(connection_string,container_name) #modification
	l=0
	print("upload file is blob storage "+container_name)
	for file in files :
		
		blob_client = container_client.get_blob_client(file.name)
		with open (file.path,'rb') as data :
			blob_client.upload_blob(data,overwrite=True,content_settings=ContentSettings(content_type='text/html'))
			

		if l!=0 :
			os.remove(file)
		l=l+1
files = get_files(path+"/link")
upload(files,key,offer)
