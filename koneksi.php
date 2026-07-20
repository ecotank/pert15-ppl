<?php
    mysqli_report(MYSQLI_REPORT_OFF);

    $host     = getenv('DB_HOST') ?: '127.0.0.1';
    $user     = getenv('DB_USER') ?: 'root'; 
    $password = getenv('DB_PASS') !== false ? getenv('DB_PASS') : '';                  
    $db       = getenv('DB_NAME') ?: 'quiz_pengupil';

    $con = @mysqli_connect($host, $user, $password);
    if (!$con) { 
        die("Connection failed: Silakan aktifkan modul MySQL pada XAMPP Control Panel! (" . mysqli_connect_error() . ")");    
    }

    // Auto-create database & table if not exists
    @mysqli_query($con, "CREATE DATABASE IF NOT EXISTS `$db`");
    @mysqli_select_db($con, $db);

    $createTableQuery = "CREATE TABLE IF NOT EXISTS `users` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `name` varchar(70) NOT NULL,
      `username` varchar(50) NOT NULL,
      `email` varchar(50) NOT NULL,
      `password` varchar(255) NOT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;";
    @mysqli_query($con, $createTableQuery);
?>