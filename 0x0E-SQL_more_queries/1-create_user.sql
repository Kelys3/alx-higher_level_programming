-- Creates the user_0d_1
-- user_0d_1 has access to all privileges o my MySQL server
-- password is set to (user_0d_1_pwd)
CREATE USER
    IF NOT EXISTS 'user_0d_1'@'localhost'
    IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES
   ON *.*
   TO 'user_0d_1'@'localhost';
