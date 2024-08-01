<?php
// submit_comment.php
$servername = "localhost";
$username = "lorinta_comments";
$password = "comments";
$dbname = "lorinta_comments";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST['username'];
    $comment = $_POST['comment'];

    $sql = "INSERT INTO comments (username, comment) VALUES ('$username', '$comment')";

    if ($conn->query($sql) === TRUE) {
        echo "正常に送信されました！ブラウザバックしてください....";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }

    $conn->close();
    exit();
}
?>