CREATE DATABASE IF NOT EXISTS lorinta_comments;
USE lorinta_comments;

CREATE TABLE IF NOT EXISTS comments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    comment TEXT NOT NULL
);
