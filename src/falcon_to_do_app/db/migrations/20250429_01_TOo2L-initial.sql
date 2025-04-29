-- Initial
-- depends: 

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE roles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    is_admin BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE user_roles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user INT NOT NULL
        REFERENCES users(username),
    role INT NOT NULL
        REFERENCES roles(name),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user, role)
);

CREATE TABLE todo_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    note VARCHAR(255) NOT NULL,
    user_id INT NOT NULL
        REFERENCES users(id),
    completed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO roles (name, is_admin)
VALUES ('admin', TRUE),
       ('user', FALSE);

INSERT INTO users (username, email)
VALUES ('admin', 'admin@example.com'),
       ('user1', 'user1@example.com'),
       ('user2', 'user2@example.com');

INSERT INTO user_roles (user, role)
VALUES ('admin', 'admin'), -- admin is an admin
       ('user1', 'user'), -- user1 is a regular user
       ('user2', 'user'); -- user2 is a regular user
