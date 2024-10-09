CREATE TABLE games (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    description TEXT
);

INSERT INTO games (name, description) VALUES
('Addition', 'A fun game where you can practice adding numbers together! Great for improving your math skills.'),
('Subtraction', 'A cool game that helps you learn how to subtract numbers! Perfect for building confidence in math.'),
('Division', 'An exciting game where you can learn how to divide numbers! Makes learning fun and easy.'),
('Multiplication', 'A game that makes multiplying numbers fun for you! Helps you master your multiplication tables.');
