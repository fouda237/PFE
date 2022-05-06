<?php

if(isset($_POST['valider'])){
    if(isset($_POST['localFiledb'])  AND isset($_POST['localFilephp']) AND isset($_POST['remoteFiledb']) AND isset($_POST['remoteFilephp'])){
        if(!empty($_POST['localFiledb']) AND !empty($_POST['localFilephp']) AND !empty($_POST['remoteFiledb']) AND !empty($_POST['remoteFilephp'])){
            $localFilevar=htmlspecialchars($_POST['localFiledb']);
            $localFilephp=htmlspecialchars($_POST['localFilephp']);
            $remoteFilevar=htmlspecialchars($_POST['remoteFiledb']);
            $remoteFilephp= htmlspecialchars($_POST['remoteFilephp']);
             
        }
    }
}
// $localFile='C:/xampp/htdocs/projet/test3.php';
$remoteFile='/var/www/html/'.$remoteFilephp;
$host = "172.104.237.137";
$port = 22;
$user = "root";
$pass = "Jjkedjke345jkJ";
$connection = ssh2_connect($host, $port);
// print $remoteFile;
// print $remoteFilevar;
// print $localFilevar;
// print $localFilephp;
// C:/xampp/htdocs/projet/test.php
if(ssh2_auth_password($connection, $user, $pass)){
    echo "connected\n";
    ssh2_scp_send($connection, $localFilevar, $remoteFilevar);
   
    ssh2_scp_send($connection, $localFilephp, $remoteFile);
     echo "done <br>";
     print "http://172.104.237.137/".$remoteFilephp;
} else {
    echo "connection failed\n";
}
?>