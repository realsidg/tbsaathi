<?php
$host="localhost";
$dbusername="root";
$dbpassword="";
$dbname="tbsaathi";
 
$fir = filter_input(INPUT_POST, 'firstName');
$las = filter_input(INPUT_POST, 'lastName');
$ema	= filter_input(INPUT_POST, 'email');
$age= filter_input(INPUT_POST, 'Age');
$gen= filter_input(INPUT_POST, 'Gender');
$add= filter_input(INPUT_POST, 'address');
$sta= filter_input(INPUT_POST, 'state');
$zip= filter_input(INPUT_POST, 'zip');
$sym= filter_input(INPUT_POST, 'zip');
$com= filter_input(INPUT_POST, 'comment');

$conn= new mysqli ($host, $dbusername, $dbpassword, $dbname);

$sql="INSERT INTO tbsaathi (First_Name,Last_Name,Email ,Age,Gender,Address,State,Zip,Symptoms,Comments) values ('$fir', '$las','$ema','$age','$gen','$add','$sta','$zip','$sym','$com')";
	if ($conn->query($sql)){

	}
	else{
		echo"Error:".$sql."<br>".$conn->error;
	}

$conn->close();
?>