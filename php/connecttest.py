from setuptools import setup
import paramiko
client=paramiko.SSHClient()
fichier=PHP("require'C:/Users/fouda/OneDrive/Bureau/php/test3.php'")
fichier.write()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname='170.187.138.38',username='root',password='Jjkedjke345jkJ',allow_agent=False,look_for_keys=False)
remotepath='/var/www/html/test.php'
localpath='C:/Users/Administrator/Desktop/php/test3.php'
sftp=client.open_sftp()
sftp.put(localpath,remotepath)
sftp.close()