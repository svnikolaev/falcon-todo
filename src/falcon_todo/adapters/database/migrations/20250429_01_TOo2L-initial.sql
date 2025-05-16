-- Initial
-- depends: 

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE roles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) NOT NULL UNIQUE,
    is_admin BOOLEAN DEFAULT FALSE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE user_roles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user INT NOT NULL
        REFERENCES users(username),
    role INT NOT NULL
        REFERENCES roles(name),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user, role)
);

CREATE TABLE todo_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INT NOT NULL
        REFERENCES users(id),
    task VARCHAR(255) NOT NULL,
    completed BOOLEAN DEFAULT FALSE,
    is_active BOOLEAN DEFAULT TRUE,
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

INSERT INTO todo_items (user_id, task, completed, is_active)
VALUES 
    (1, 'Complete initial setup', FALSE, TRUE),
    (2, 'Review database schema', FALSE, TRUE),
    (3, 'Test API endpoints', FALSE, TRUE),
    (1, 'Configure user roles', FALSE, TRUE),
    (2, 'Implement authentication', FALSE, TRUE),
    (3, 'Setup CI/CD pipeline', FALSE, TRUE);
