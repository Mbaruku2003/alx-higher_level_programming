-- creates the table unique_id
-- unique_id descriptiond INTDEFAULT IS 1
-- name VARCHAR(256)
--table unique id
CREATE table IF NOT EXISTS unique_id
	(id INT DEFAULT 1, UNIQUE(ID), name VARCHAR(256));
