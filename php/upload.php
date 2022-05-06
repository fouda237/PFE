<?php
$localFile='C:/Users/Administrator/Desktop/php/test3.php';
$remoteFile='/var/www/html/test1.php';
$host = "172.104.237.137";
$port = 22;
$user = "root";
$pass = "Jjkedjke345jkJ";
 
$connection = ssh2_connect($host, $port);
ssh2_auth_password($connection, $user, $pass);
$sftp = ssh2_sftp($connection);
 
$stream = fopen("ssh2.sftp://$sftp$remoteFile", 'w');
$file = file_get_contents($localFile);
fwrite($stream, $file);
fclose($stream);
?>
