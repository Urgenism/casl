-- Database: `tipproject`

-- Table structure for table `Games`

CREATE TABLE Games (
    IdGame INT AUTO_INCREMENT PRIMARY KEY,
    IdQuestion INT,
    Name VARCHAR(255) NOT NULL,
    Type VARCHAR(100),
    NoOfQuestion INT
);

--
-- Dumping data for table `Games`
--
INSERT INTO Games (IdQuestion, Type, NoOfQuestion)
VALUES
(1, 'Addition', 10),
(2, 'Subtraction', 10),
(3, 'Multiplication', 10),
(4, 'Division', 10);

-- Table structure for table `Question`
CREATE TABLE Question (
    IdQuestion INT AUTO_INCREMENT PRIMARY KEY,
    IdGame INT,
    Description TEXT NOT NULL,
    Options TEXT NOT NULL,
    CorrectAnswer VARCHAR(255) NOT NULL,
    FOREIGN KEY (IdQuestion) REFERENCES Games(IdQuestion)
);

-- Dumping data for table `Question`

INSERT INTO Question (IdQuestion, Description, Options, CorrectAnswer)
VALUES
(1, 'What is 7 + 3?', 'A. 6, B. 10, C. 3, D. 9', 'B. 10'),
(1, 'What is 10 + 4?', 'A. 6, B. 8, C. 14, D. 12', 'C. 14'),
(1, 'What is 5 + 3?', 'A. 6, B. 7, C. 8, D. 9', 'C. 8'),
(1, 'What is 10 + 15?', 'A. 15, B. 25, C. 27, D. 18', 'B. 25'),
(1, 'What is 12 + 2?', 'A. 22, B. 14, C. 26, D. 28', 'B. 14'),
(1, 'What is 18 + 13?', 'A. 45, B. 30, C. 37, D. 28', 'B. 30'),
(1, 'What is 10 + 7?', 'A. 19, B. 13, C. 25, D. 17', 'D. 17'),
(1, 'What is 12 + 13?', 'A. 42, B. 23, C. 25, D. 35', 'C. 25'),
(1, 'What is 7 + 6?', 'A. 13, B. 12, C. 8, D. 14', 'A. 13'),
(1, 'What is 12 + 5?', 'A. 22, B. 13, C. 17, D. 25', 'C. 17'),
(2, 'What is 15 - 9?', 'A. 16, B. 26, C. 27, D. 28', 'A. 16'),
(2, 'What is 9 - 2?', 'A. 6, B. 11, C. 7, D. 10', 'C. 7'),
(2, 'What is 20 - 4?', 'A. 13, B. 16, C. 14, D. 17', 'B. 16'),
(2, 'What is 13 - 2?', 'A. 14, B. 16, C. 11, D. 13', 'C. 11'),
(2, 'What is 19 - 2?', 'A. 16, B. 11, C. 17, D. 12', 'C. 17'),
(2, 'What is 11 - 4?', 'A. 5, B. 7, C. 8, D. 10', 'B. 7'),
(2, 'What is 10 - 5?', 'A. 4, B. 6, C. 5, D. 3', 'C. 5'),
(2, 'What is 15 - 2?', 'A. 23, B. 13, C. 33, D. 15', 'B. 13'),
(2, 'What is 18 - 3?', 'A. 15, B. 16, C. 14, D. 20', 'A. 15'),
(2, 'What is 20 - 7?', 'A. 24, B. 26, C. 13, D. 12', 'C. 13'),
(3, 'What is 7 x 2?', 'A. 14, B. 15, C. 18, D. 30', 'A. 14'),
(3, 'What is 5 x 4?', 'A. 20, B. 21, C. 28, D. 13', 'A. 20'),
(3, 'What is 3 x 2?', 'A. 4, B. 6, C. 2, D. 3', 'B. 6'),
(3, 'What is 7 x 5?', 'A. 20, B. 25, C. 35, D. 30', 'C. 35'),
(3, 'What is 4 x 4?', 'A. 24, B. 15, C. 18, D. 16', 'D. 16'),
(3, 'What is 6 x 5?', 'A. 30, B. 20, C. 37, D. 32', 'A. 30'),
(3, 'What is 8 x 2?', 'A. 8, B. 16, C. 14, D. 24', 'B. 16'),
(3, 'What is 4 x 7?', 'A. 24, B. 25, C. 20, D. 28', 'D. 28'),
(3, 'What is 6 x 3?', 'A. 18, B. 14, C. 12, D. 13', 'A. 18'),
(3, 'What is 9 x 4?', 'A. 36, B. 30, C. 24, D. 38', 'A. 36'),
(4, 'What is 20 ÷ 4?', 'A. 4, B. 5, C. 6, D. 7', 'B. 5'),
(4, 'What is 12 ÷ 3?', 'A. 2, B. 3, C. 4, D. 5', 'C. 4'),
(4, 'What is 18 ÷ 3?', 'A. 5, B. 6, C. 7, D. 8', 'B. 6'),
(4, 'What is 15 ÷ 5?', 'A.3, B. 2, C. 4, D. 5', 'A. 3'),
(4, 'What is 6 ÷ 2?', 'A. 1, B. 2, C. 3, D. 4', 'C. 3'),
(4, 'What is 10 ÷ 2?', 'A. 8, B. 2, C. 3, D. 5', 'D. 5'),
(4, 'What is 25 ÷ 5?', 'A. 2, B. 5, C. 8, D. 10', 'B. 5'),
(4, 'What is 12 ÷ 4?', 'A. 3, B. 7, C. 2, D. 5', 'A. 3'),
(4, 'What is 27 ÷ 9?', 'A. 9, B. 6, C. 5, D. 3', 'D. 3'),
(4, 'What is 32 ÷ 8?', 'A. 2, B. 4, C. 6, D. 8', 'B. 4');


-- Table structure for table `Result`
CREATE TABLE Result (
    IdResult INT AUTO_INCREMENT PRIMARY KEY,
    IdGame INT UNIQUE,
    Id INT,
    Score INT,
    TotalQuestions INT,
    CorrectAnswer INT,
    FOREIGN KEY (IdGame) REFERENCES Games(IdGame),
    FOREIGN KEY (Id) REFERENCES Users(Id)
);