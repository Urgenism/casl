CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    role ENUM('student', 'teacher', 'admin') NOT NULL, 
    class_id VARCHAR(50) 
    is_active TINYINT(1) DEFAULT 0
);