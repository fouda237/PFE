from linode_api4 import LinodeClient
import time
import paramiko
from clrprint import *
all_ipp=[]
client = LinodeClient("ee60e6f681266390d1157edc80d093d5f72bc2cea710ce800a96e490c714bb90")

i=0

available_instances = client.linode.instances()

for instance in available_instances:
    all_ipp.append(instance.ipv4[0])


command1 = "telnet 170.187.138.38"
command = "yum install telnet telnet-server -y"
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


for ip in all_ipp :
  try:
    #while(key):
         print(ip)
         print("Start SSH")
         ssh.connect(str(ip), 22, "root", "Jjkedjke345jkJ")
         stdin, stdout, stderr = ssh.exec_command(command)
  except:
    print("An exception occurred")
    continue
print("10 seconde")
time.sleep(10)
    
available_instances = client.linode.instances()
for instance in available_instances:
  try:
         print(all_ipp[i])
         print("Start SSH")
         try:
          response="nono"
          ssh.connect(str(all_ipp[i]), 22, "root", "Jjkedjke345jkJ")
          stdin, stdout, stderr = ssh.exec_command(command1)
          lines = stdout.readlines()
          response = lines[3][0:3]
          i=i+1
         except:
             print("lala")
         if response == "220":
           clrprint("ok",clr='green')
         elif  response == "554":
           clrprint("delete",clr='red')
           instance.delete()

          
         else:
           print("non")               
  except:
    print("An exceptin ")
    continue
