-- creates the MySQL server user user_0d_1.
-- user_0d_1 should have all privileges
-- user_0d_1 password should be set to user_0d_1_pwd
-- user_0d_1 already exists, your script should not fail
CREATE user IF NOT EXISTS user_0d_1
GRANT ALL
ON *.*
TO 'user_0d_1'@'localhost';
