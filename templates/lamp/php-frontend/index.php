<?php
$host = 'mysql-db';
$user = 'root';
$pass = 'password';
$db = 'testdb';

$conn = new mysqli($host, $user, $pass, $db);

if ($conn->connect_error) {
    die("❌ Connection failed: " . $conn->connect_error);
}
echo "✅ Connected to MySQL successfully!<br>";

$result = $conn->query("SELECT * FROM users");

if ($result->num_rows > 0) {
    while($row = $result->fetch_assoc()) {
        echo "👤 " . $row["name"] . "<br>";
    }
} else {
    echo "🚫 No users found.";
}
$conn->close();
?>
