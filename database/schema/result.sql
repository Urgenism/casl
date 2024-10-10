CREATE TABLE result (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_user INT NOT NULL, -- foreign key referencing the users table
    id_game INT NOT NULL, -- foreign key referencing the games table
    score INT NOT NULL, -- the score the user achieved in the game
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- timestamp of when the result was created
    CONSTRAINT fk_user_result FOREIGN KEY (id_user) REFERENCES users(id), -- foreign key constraint for users
    CONSTRAINT fk_game_result FOREIGN KEY (id_game) REFERENCES games(id)  -- foreign key constraint for games
);
