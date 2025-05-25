CREATE TABLE IF NOT EXISTS users 
                (id SERIAL, 
                email VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL, 
                username VARCHAR(255), 
                verified BOOLEAN DEFAULT FALSE);

CREATE TABLE IF NOT EXISTS groups 
                    (id SERIAL,
                    title VARCHAR(255) NOT NULL,
                    admin_id integer NOT NULL);

CREATE TABLE IF NOT EXISTS members 
                (
                    group_id integer NOT NULL,
                    user_id integer NOT NULL
                );

CREATE TABLE IF NOT EXISTS messages 
                (
                    id SERIAL, 
                    author VARCHAR(255) NOT NULL, 
                    user_id integer NOT NULL, 
                    content VARCHAR, 
                    group_id integer NOT NULL,
                    code VARCHAR(255) NOT NULL,
                    created_at VARCHAR(255) NOT NULL
                );

INSERT INTO users
            (email, username, password, verified)
            VALUES
            (
                'aleks_01_@gmail.com',
                'administrator',
                'admin',
                TRUE
            );

INSERT INTO users
            (email, username, password, verified)
            VALUES
            (
                'reset-password@gmail.com',
                'test-01',
                'test',
                TRUE
            );

INSERT INTO groups
                (title, admin_id) VALUES
                ('General Group Chat', 1);

INSERT INTO members
            (user_id, group_id)
            VALUES (1,1);

INSERT INTO users
            (email, username, password, verified)
            VALUES
            (
                'unverified@gmail.com',
                'administrator',
                'admin',
                FALSE
            );

INSERT INTO members
            (user_id, group_id)
            VALUES (2,1);