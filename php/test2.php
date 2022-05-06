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
	$access_key = 'a2947addf0a1bf8828b41a11cf7212ec' ;

	// Initialiser CURL :// Initialiser CURL :
	$ch = curl_init('http://api.ipstack.com/'.$IP_Connected.'?access_key='.$access_key.'');
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1); 
	
	// Stocke les données :// Stocke les données :
	$json = curl_exec($ch);
	curl_close($ch);
	
	// Décode la réponse JSON :// Décode la réponse JSON :
	$api_result = json_decode($json, true);
	print_r($api_result);
	// Sortie de l'objet "capital" à l'intérieur de "location"
	
	
	$country=$api_result["country_code"];
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
	else
	{
		 header('Location: https://imgur.com/');
		  exit();} 
		
	
?>