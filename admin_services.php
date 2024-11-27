<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $service_id = $_POST['service-id'];
    $action = $_POST['service-action'];
    $service_name = $_POST['service-name'];
    $service_description = $_POST['service-description'];
    $service_status = $_POST['service-status'];

    // Database connection
    $conn = new mysqli('localhost', 'root', '', 'student_portal');

    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    if ($action == 'insert') {
        $sql = "INSERT INTO services (service_id, name, description, status) VALUES ('$service_id', '$service_name', '$service_description', '$service_status')";
    } elseif ($action == 'update') {
        $sql = "UPDATE services SET name='$service_name', description='$service_description', status='$service_status' WHERE service_id='$service_id'";
    } elseif ($action == 'delete') {
        $sql = "DELETE FROM services WHERE service_id='$service_id'";
    }

    if ($conn->query($sql) === TRUE) {
        echo "Service action executed successfully";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }

    $conn->close();
}
?>
