CREATE TABLE result (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_user INT NOT NULL, 
    id_game INT NOT NULL, 
    score INT NOT NULL,
    feedback TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_user_result FOREIGN KEY (id_user) REFERENCES users(id),
    CONSTRAINT fk_game_result FOREIGN KEY (id_game) REFERENCES games(id) 
);
