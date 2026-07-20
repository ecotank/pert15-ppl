<?php
session_start();
if (!isset($_SESSION['username'])) {
    header('Location: login.php');
    exit();
}

if (isset($_GET['action']) && $_GET['action'] == 'logout') {
    session_destroy();
    header('Location: login.php');
    exit();
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Dashboard - Quiz Pengupil</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css">
</head>
<body class="bg-light">
    <div class="container mt-5">
        <div class="card shadow-sm">
            <div class="card-body text-center">
                <h2 class="card-title">Selamat Datang!</h2>
                <p class="card-text text-muted">Anda berhasil masuk sebagai: <strong id="welcome-user"><?= htmlspecialchars($_SESSION['username']); ?></strong></p>
                <a href="index.php?action=logout" id="logout-btn" class="btn btn-danger">Logout</a>
            </div>
        </div>
    </div>
</body>
</html>
