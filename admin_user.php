<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $user_id = $_POST['user-id'];
    $action = $_POST['user-action'];
    $user_type = $_POST['user-type'];

    // Database connection
    $conn = new mysqli('localhost', 'root', '', 'student_portal');

    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    if ($action == 'add') {
        $sql = "INSERT INTO users (user_id, user_type) VALUES ('$user_id', '$user_type')";
    } elseif ($action == 'remove') {
        $sql = "DELETE FROM users WHERE user_id='$user_id' AND user_type='$user_type'";
    }

    if ($conn->query($sql) === TRUE) {
        echo "User action executed successfully";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }

    $conn->close();
}
?>
