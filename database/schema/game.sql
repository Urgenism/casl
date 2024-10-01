CREATE TABLE Games (
    IdGame INT PRIMARY KEY AUTO_INCREMENT,
    IdQuestion INT, -- This can be used as a foreign key reference
    Name VARCHAR(255) NOT NULL,
    Description TEXT,
    Type VARCHAR(50),
    NoOfQuestion INT,
    CONSTRAINT fk_game_question FOREIGN KEY (IdQuestion) REFERENCES Question(IdQuestion)
);
