<?php
// display_comments.php
$servername = "localhost";
$username = "lorinta_comments";
$password = "comments";
$dbname = "lorinta_comments";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT username, comment, created_at FROM comments ORDER BY created_at DESC";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    while($row = $result->fetch_assoc()) {
        echo "<div class='comment'>";
        echo "<h4>" . htmlspecialchars($row['username']) . "</h4>";
        echo "<p>" . htmlspecialchars($row['comment']) . "</p>";
        echo "<small>" . $row['created_at'] . "</small>";
        echo "</div>";
    }
} else {
    echo "No comments yet!";
}

$conn->close();
?>