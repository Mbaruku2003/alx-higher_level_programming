-- creates the table id_not_null
--id_not_null description id INT with the default 1
-- and name VARCHAR(256)
-- if the table id_not_null already exist its ok
CREATE table IF NOT EXISTS id_not_null (id INT DEFAULT '1', name VARCHAR(256));
