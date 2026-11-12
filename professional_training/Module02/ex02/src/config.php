<?php 

$dbhost = "127.0.0.1";
$dbuser = "root";
$dbpass = "root";
$dbname = "mine";
$flag = getenv('FLAG');
$defaultId = 'guest';
$conn = mysqli_connect($dbhost,$dbuser,$dbpass,$dbname);


/*  
create table `users` (
    `id` int(32) auto_increment primary key,
    `username` varchar(40) not null,
    `encrypted_pass` varchar(100) not null
);

*/