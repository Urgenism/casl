CREATE TABLE question (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_game INT,
    description TEXT NOT NULL,
    option_a INT NOT NULL,
    option_b INT NOT NULL,
    option_c INT NOT NULL,
    option_d INT NOT NULL,
    correct_answer INT NOT NULL,
    CONSTRAINT fk_game FOREIGN KEY (id_game) REFERENCES games(id)
);

-- 10 easy addition questions
INSERT INTO question (id_game, description, option_a, option_b, option_c, option_d, correct_answer) VALUES
(1, 'What is 5 + 3?', 7, 9, 10, 8, 8),
(1, 'What is 10 + 4?', 13, 12, 14, 15, 14),
(1, 'What is 7 + 6?', 12, 14, 11, 13, 13),
(1, 'What is 8 + 2?', 10, 9, 12, 11, 10),
(1, 'What is 9 + 7?', 16, 14, 15, 17, 16),
(1, 'What is 12 + 5?', 19, 18, 17, 16, 17),
(1, 'What is 3 + 8?', 12, 14, 13, 11, 11),
(1, 'What is 6 + 9?', 14, 13, 15, 16, 15),
(1, 'What is 4 + 4?', 7, 8, 9, 6, 8),
(1, 'What is 15 + 5?', 21, 19, 18, 20, 20);


-- 10 Easy Subtraction Questions
INSERT INTO question (id_game, description, option_a, option_b, option_c, option_d, correct_answer) VALUES
(2, 'What is 9 - 4?', 5, 6, 4, 3, 5),
(2, 'What is 15 - 7?', 8, 9, 10, 7, 8),
(2, 'What is 20 - 5?', 16, 15, 13, 14, 15),
(2, 'What is 18 - 9?', 7, 9, 10, 8, 9),
(2, 'What is 10 - 3?', 7, 6, 9, 8, 7),
(2, 'What is 22 - 11?', 12, 11, 10, 13, 11),
(2, 'What is 13 - 6?', 6, 7, 5, 8, 7),
(2, 'What is 30 - 12?', 18, 16, 17, 15, 18),
(2, 'What is 25 - 10?', 16, 15, 14, 13, 15),
(2, 'What is 8 - 5?', 3, 5, 4, 2, 3);


-- 10 Easy Division Questions
INSERT INTO question (id_game, description, option_a, option_b, option_c, option_d, correct_answer) VALUES
(3, 'What is 8 ÷ 4?', 1, 2, 3, 4, 2),
(3, 'What is 12 ÷ 6?', 2, 1, 3, 4, 2),
(3, 'What is 18 ÷ 9?', 1, 3, 2, 4, 2),
(3, 'What is 20 ÷ 5?', 4, 2, 3, 5, 4),
(3, 'What is 16 ÷ 4?', 2, 4, 3, 1, 4),
(3, 'What is 9 ÷ 3?', 4, 3, 2, 1, 3),
(3, 'What is 24 ÷ 8?', 2, 4, 3, 1, 3),
(3, 'What is 50 ÷ 10?', 6, 7, 5, 4, 5),
(3, 'What is 30 ÷ 5?', 6, 7, 5, 4, 6),
(3, 'What is 45 ÷ 9?', 3, 4, 5, 2, 5);


-- 10 Easy Multiplication Questions
INSERT INTO question (id_game, description, option_a, option_b, option_c, option_d, correct_answer) VALUES
(4, 'What is 3 x 4?', 12, 10, 14, 13, 12),
(4, 'What is 5 x 6?', 25, 30, 35, 40, 30),
(4, 'What is 7 x 8?', 49, 54, 56, 64, 56),
(4, 'What is 6 x 9?', 54, 48, 60, 72, 54),
(4, 'What is 9 x 3?', 18, 21, 27, 24, 27),
(4, 'What is 4 x 8?', 24, 32, 36, 28, 32),
(4, 'What is 12 x 12?', 144, 132, 150, 128, 144),
(4, 'What is 8 x 7?', 49, 56, 63, 48, 56),
(4, 'What is 10 x 10?', 90, 100, 110, 120, 100),
(4, 'What is 11 x 2?', 22, 33, 44, 55, 22);
