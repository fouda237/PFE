import pysftp as sftp
import crypto
import paramiko

def sftpExample():
    try:
        s=sftp.Connection(hostname='170.187.138.38:22',username='root',password='Jjkedjke345jkJ')
        remotepath='/var/www/html/t1.php'
        localpath='C:/Users/Administrator/desktop/php/test3.php'
        s.put(localpath,remotepath)
        s.close()
    except Exception as e:
        print('failed main', str(e))
sftpExample()    