CREATE TABLE Result (
    IdResult INT PRIMARY KEY AUTO_INCREMENT,
    IdGame INT, -- Foreign key referencing the Games table
    IdUser INT, -- Assuming this refers to a user in a User table
    Score INT NOT NULL,
    TotalQuestions INT NOT NULL,
    CorrectAnswer INT NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (IdGame) REFERENCES Games(IdGame)
);