<?php
$a='FR';
$b='RU';
$c='DE';
$alien='https://www.youtube.com/';
$blien='https://www.google.com/';
$clien= 'https://www.netflix.com/watch/0?origId=80002565';
$dlien='https://flask.palletsprojects.com/en/2.0.x/';
 
?>
       <?php
        // $localhost="localhost"; #localhost
        // $username="zferwrgy_ipgeo"; # username
        // $password="Digitacon212"; # password
        // $dbname="zferwrgy_ipgeo"; #database name
        // #connection string
        // $conn=mysqli_connect($localhost,$username, $password, $dbname);
        //define PDO - tell about the database file
          $pdo=new PDO('sqlite:movies.db');
          $pdo->exec("CREATE TABLE Links(id INTEGER PRIMARY KEY AUTOINCREMENT,Link TEXT,code_country TEXT );");
        if(isset($_POST['valider'])){
          if(isset($_POST['a'])  AND isset($_POST['alien']) AND isset($_POST['b']) AND isset($_POST['blien'])  AND isset($_POST['c'])  AND isset($_POST['clien']) AND isset($_POST['dlien'])){
            if(!empty($_POST['a']) AND !empty($_POST['alien']) AND !empty($_POST['b']) AND !empty($_POST['blien']) AND !empty($_POST['c']) AND !empty($_POST['clien']) AND !empty($_POST['dlien'])){
            $a=$_POST['a'];
            $alien=$_POST['alien']; 
            $b=$_POST['b'];
            $blien=$_POST['blien'];
            $c=$_POST['c'];
            $clien=$_POST['clien'];
            $dlien=$_POST['dlien'];
            try{
            $pdo->exec("INSERT INTO  Links(Link,code_country) VALUES('$alien','$a');");
            $pdo->exec("INSERT INTO  Links(Link,code_country) VALUES('$blien','$b');");
            $pdo->exec("INSERT INTO Links(Link,code_country) VALUES('$clien','$c');");
            $pdo->exec("INSERT INTO Links(Link,code_country) VALUES('$dlien','');");
             echo "inserer";
            }catch(PDOException $e){
              echo $e->getMessage();
            }
            }
          }
         
        }
        ?>
        
    // $statement4 =$pdo->query("SELECT Link FROM Links WHERE ID=4");
    // $dlien=$statement1->fetchColumn();
    // $statementa =$pdo->query("SELECT code_country FROM Links WHERE ID=1");
    // $a=$statementa->fetchColumn();
    // $statementb =$pdo->query("SELECT code_country FROM Links WHERE ID=2");
    // $b=$statementb->fetchColumn();
    // $statementc =$pdo->query("SELECT code_country FROM Links WHERE ID=3");
    // $c=$statementc->fetchColumn();
//     if ($country3==$a)
//     { 
//        header('Location:'.$lien);
//      exit();
//     } 
// elseif ($country3==$b)
//   {
//      header('Location:'.$blien);
//     exit(); 
//  } 
// elseif ($country3==$c) 
//  { 
//     header('Location:'.$clien);
//   exit();
// } 
// else
//  {
//    header('Location:'.$dlien);
//    exit();
// } 
    // if($country1=!$country2 && $country1=!$country3 && $country2=!$country3){
    //     if ($country3==$_POST['a'])
	//     { 
	// 	   header('Location:'.$_POST['alien']);
	//      exit();
	//     } 
    // elseif ($country3==$_POST['b'])
 	//  {
	// 	 header('Location:'.$_POST['blien']);
 	//    exit(); 
    //  } 
    // elseif ($country3==$_POST['c']) 
 	// { 
	// 	header('Location:'.$_POST['clien']);
 	//  exit();
    // } 
    // else
    //  {
	//    header('Location:'.$_POST['dlien']);
 	//   exit();
    // } 

    // }else{
    //      // condiction FR
	//     if ((($country1 && $country2)or($country2&& $country3)or($country1 && $country3))==$_POST['a'])
		 
    //      { 
    //        header('Location:'.$_POST['alien']);
    //      exit();
    //      } 
    //     //condiction NL
    //     elseif ((($country1 && $country2)or($country2&& $country3)or($country1 && $country3))==$_POST['b'])
    
    //      { 
    //        header('Location: '.$_POST['blien']);
    //       exit();
    //      } 
    //      //condiction RU                   
    //     elseif ((($country1 && $country2)or($country2&& $country3)or($country1 && $country3))==$_POST['c'])
    
    //      { 
    //         header('Location:'.$_POST['clien']);
    //      exit();
    //      }else
    //      {
    //        header('Location:'.$_POST['dlien']);
    //        exit();}
    //   } 