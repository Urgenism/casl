CREATE TABLE question (
    id INT PRIMARY KEY AUTO_INCREMENT,
    idGame INT,
    description TEXT NOT NULL,
    options JSON NOT NULL,   -- Assume JSON or comma-separated format for options
    correctAnswer VARCHAR(50) NOT NULL,
    CONSTRAINT fk_game FOREIGN KEY (idGame) REFERENCES games(id)
);