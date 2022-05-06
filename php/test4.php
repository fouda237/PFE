<?php
 /* banned IP */ 
$IP_Connected = $_SERVER['REMOTE_ADDR']; 
$IP_Banned=array();
 foreach($IP_Banned as $Ip_word) { 
    if ( @substr_count($IP_Connected, $Ip_word) > 0) { 
	    echo "<h1>Access Denied</h1>"; 
	    exit();
    } 
    
 }

 /* DENIED HOST */ 
$HostName = gethostbyaddr($_SERVER['REMOTE_ADDR']); 
$Blocked_keywords=array();
 foreach($Blocked_keywords as $keyword) { 
    if ( @substr_count($HostName, $keyword) > 0) { 
	    echo "<h1>Access Denied</h1>"; 
	    exit();
    } 
 }
 /* DENIED USERAGENT */ 
$UserAgent = $_SERVER['HTTP_USER_AGENT']; 
$UserAgent_blocked=array();
foreach($UserAgent_blocked as $Agent_bot) {
	 if (substr_count($UserAgent, $Agent_bot) > 0) {
		 echo "<h1>Access Denied</h1>";
		 exit(); 
		} 
	}

// $access_key = 'API_ACCESS_KEY';
$url = "https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyA18ApKhdJ2_Gzx1x6PHSQNqQanqwEXuCw";
$ch = curl_init();  
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_URL, $url);
$response = curl_exec($ch);
if (curl_errno($ch)) {
    $error_msg = curl_error($ch);
    echo $error_msg;
}
$arr_result = json_decode($response, true);
//print_r($arr_result);
$country=$arr_result["country_code2"];
print_r($country);
if ($country=="FR")
     
	 { 
		 header('Location: https://www.google.com/');
	 exit();
	} 
elseif ($country=="NL")
    
 	{
		 header('Location: https://www.youtube.com/');
 	 exit();} 
 elseif ($country=="RU") 
 	{ 
		header('Location: https://translate.google.co.ma/');
 	 exit();} 
elseif ($country=="US") 
      { 
         header('Location: https://translate.google.US/');
       exit();} 
else
{
	 header('Location: https://imgur.com/');
 	 exit();} 
	
?>