CREATE TABLE Question (
    IdQuestion INT PRIMARY KEY AUTO_INCREMENT,
    IdGame INT, -- This will act as a foreign key from the Games table
    Description TEXT NOT NULL,
    Options TEXT, -- Can be JSON or comma-separated values, depending on your choice
    CorrectAnswer VARCHAR(255) NOT NULL,
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
