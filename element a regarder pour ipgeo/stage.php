<!DOCTYPE html>
<html lang="en">
<head>
    <title>Document</title>
    <link rel="stylesheet" href="stage.css">
</head>
<body>
  <div>
      <form action="" method="post" class="post">
        <div> 
            <div>
            <div class="container">
                    <label for="cars">Nom de la table</label>
                      <br>
                         <input type="text" id="Lien" name="Links" placeholder="Table" autocomplete="off" />
                   </div>
                <div class="container">
                    <label for="cars">Lien</label>
                      <br>
                         <input type="text" id="Lien" name="Lien1" placeholder="Lien" autocomplete="off" />
                   </div>
                   <div class="lo">
                    <label for="cars">Code Country</label>
                      <br>
                         <input type="text" id="Code_country" name="Code_country1" placeholder="Code_country"  autocomplete="off" />
                   </div>
                </div> 
            <div>
                <div class="">
                    <label for="cars">Lien</label>
                      <br>
                         <input type="text" id="Lien" name="Lien2" placeholder="Lien" autocomplete="off" />
                   </div>
                   <div class="lo">
                    <label for="cars">Code Country</label>
                      <br>
                         <input type="text" id="Code_country" name="Code_country2" placeholder="Code_country"  autocomplete="off" />
                   </div>
                </div> 
                <div>
                    <div class="">
                        <label for="cars">Lien</label>
                          <br>
                             <input type="text" id="Lien" name="Lien3" placeholder="Lien" autocomplete="off" />
                       </div>
                       <div class="lo">
                        <label for="cars">Code Country</label>
                          <br>
                             <input type="text" id="Code_country" name="Code_country3" placeholder="Code_country"  autocomplete="off" />
                       </div>
                    </div> 
                    <div>
                        <div class="">
                            <label for="cars">Lien</label>
                              <br>
                                 <input type="text" id="Lien" name="Lien4" placeholder="Lien" autocomplete="off" />
                           </div>
                           <div class="lo">
                            <label for="cars">Code Country</label>
                              <br>
                                 <input type="text" id="Code_country" name="Code_country4" placeholder="Code_country"  autocomplete="off" />
                           </div>
                        </div> 
                <div class="jom">
                    <button type="submit" name="insert" >Insert</button>  
                    <button type="submit" name="delect" >Delect</button> 
                </div> 
            </div> 
      </form>
      <?php
        // $localhost="localhost"; #localhost
        // $username="zferwrgy_ipgeo"; # username
        // $password="Digitacon212"; # password
        // $dbname="zferwrgy_ipgeo"; #database name
        // #connection string
        // $conn=mysqli_connect($localhost,$username, $password, $dbname);
        //define PDO - tell about the database file
          $pdo=new PDO('sqlite:movies.db');
         
        if(isset($_POST['insert'])){
          if(isset($_POST['Links'])  AND  isset($_POST['Code_country1'])  AND isset($_POST['Lien1']) AND isset($_POST['Code_country2']) AND isset($_POST['Lien2'])  AND isset($_POST['Code_country3'])  AND isset($_POST['Lien3']) AND isset($_POST['Code_country4']) AND isset($_POST['Lien4'])){
            if( !empty($_POST['Links']) AND !empty($_POST['Code_country1']) AND !empty($_POST['Lien1']) AND !empty($_POST['Code_country2']) AND !empty($_POST['Lien2']) AND !empty($_POST['Code_country3']) AND !empty($_POST['Lien3']) AND !empty($_POST['Code_country4']) AND !empty($_POST['Lien4'])){
            $a=$_POST['Code_country1'];
            $alien=$_POST['Lien1']; 
            $b=$_POST['Code_country2'];
            $blien=$_POST['Lien2'];
            $c=$_POST['Code_country3'];
            $clien=$_POST['Lien3'];
            $d=$_POST['Code_country4'];
            $dlien=$_POST['Lien4'];
            $links=$_POST['Links'];
            try{
            $pdo->exec("CREATE TABLE $links(id INTEGER PRIMARY KEY AUTOINCREMENT,Link TEXT,code_country TEXT );");
            $pdo->exec("INSERT INTO  Links(Link,code_country) VALUES('$alien','$a');");
            $pdo->exec("INSERT INTO  Links(Link,code_country) VALUES('$blien','$b');");
            $pdo->exec("INSERT INTO Links(Link,code_country) VALUES('$clien','$c');");
            $pdo->exec("INSERT INTO Links(Link,code_country) VALUES('$dlien','$d');");
             echo "inserer";
            }catch(PDOException $e){
              echo $e->getMessage();
            }
            }
          }
         
        }
        if(isset($_POST['delect'])){
          try{
            $pdo->exec("DROP TABLE Links;");
            echo "supprimer";
          }catch(PDOException $e){
            echo $e->getMessage();
          }
        }
        ?>
        <br>
        <br>
    <form action="upload1.php" class="fom" method="post">
    <div> 
        <div>
            <div class="">
                <label for="cars">localFiledb</label>
                  <br>
                     <input type="text" id="localFile" name="localFiledb" value="C:/xampp/htdocs/projet/" autocomplete="off" />
               </div>
               <div class="lo">
                <label for="cars">RemoteFiledb</label>
                  <br>
                     <input type="text" id="remoteFile" name="remoteFiledb" value="/var/www/html/movies.db"  autocomplete="off" />
               </div>
            </div> 
        <div>
            <div class="">
                <label for="cars">LocalFilephp</label>
                  <br>
                     <input type="text" id="localFile" name="localFilephp" value="C:/xampp/htdocs/projet/" autocomplete="off" />
               </div>
               <div class="lo">
                <label for="cars">RemoteFilephp</label>
                  <br>
                     <input type="text" id="remoteFile" name="remoteFilephp"   autocomplete="off" />
               </div>
            </div> 
            <div class="jom">
                <button type="submit" name="valider" >Upload</button>
            </div> 
        </div> 
      </form>
  </div>
</body>
</html>