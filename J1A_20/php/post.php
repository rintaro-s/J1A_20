<?php

// データベース接続
$db = new PDO('sqlite:comment.db');

// コメントを投稿
if (isset($_POST['name']) && isset($_POST['comment'])) {
  $name = htmlspecialchars($_POST['name']);
  $comment = htmlspecialchars($_POST['comment']);
  $date = date('Y-m-d H:i:s');

  // SQL文
  $sql = "INSERT INTO comments (name, comment, date) VALUES (:name, :comment, :date)";
  $stmt = $db->prepare($sql);
  $stmt->bindParam(':name', $name);
  $stmt->bindParam(':comment', $comment);
  $stmt->bindParam(':date', $date);
  $stmt->execute();

  // コメントをファイルに保存
  $fp = fopen('https://lorinta.xsrv.jp/wp-content/uploads/html_study/comment.txt', 'a');
  fwrite($fp, $name . ": " . $comment . " (" . $date . ")\n");
  fclose($fp);

  // リダイレクト
  header('Location: index.html');
  exit;
}

?>
