import paramiko,os
from io import StringIO
host=22
port="170.187.138.38"
transport=paramiko.Transport((host,port))
# username='root'
# key='Jjkedjke345jkJ'
# with open(key) as f:
#     fin=f.read()
# final_key=StringIO(fin)
# keyFile=paramiko.RSAKey.from_private_key(final_key) 
# transport=paramiko.Transport((host,port))
# transport.connect( username=username,pkey=keyFile)   
# sftp=paramiko.SFTPClient.from_transport(transport)

# #sftp.put('testfile.txt','testfile.txt')
# sftp.get('test1.txt','text1.txt')