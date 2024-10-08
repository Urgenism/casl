CREATE TABLE Games (
    IdGame INT PRIMARY KEY AUTO_INCREMENT,
    IdQuestion INT,
    Game_Name VARCHAR(255) NOT NULL,
    Game_Description TEXT,
    Game_Type VARCHAR(50),
    NoOfQuestion INT,
    FOREIGN KEY (IdQuestion) REFERENCES Question(IdQuestion)
);