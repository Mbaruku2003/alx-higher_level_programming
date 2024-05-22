-- creates the table force_name
-- forc_name description id INT and name(VARCHAR(256) AND CANT BE NULL
-- If the table force_name already exists, your script should not faiL
CREATE table IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL)
