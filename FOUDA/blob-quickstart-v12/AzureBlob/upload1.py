import os
import yaml
from azure.storage.blob import ContainerClient



def load_config():
    dir_root = os.path.dirname(os.path.abspath(__file__))
    with open (dir_root + "\\config.yaml","r") as yamlfile:
     return yaml.load(yamlfile, Loader=yaml.FullLoader)

config = load_config()
print(* config)

# def get_files(dir):
#   with os.scandir(dir) as entries :
#     for entry in entries:
#       if entry.is_file() and not entry.name.startswith('.'):
#         yield entry

# config = load_config()
# print(* config)