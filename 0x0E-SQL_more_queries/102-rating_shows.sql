-- lists all shows from hbtn_0d_tvshows_rate by their rating.
CREATE TABLE IF NOT EXISTS temp_july_aug
	SELECT *
	FROM temperatures
	WHERE month = 7 OR month = 8;
SELECT city, AVG(value) AS avg_temp
FROM temp_july_aug
GROUP BY city
ORDER BY avg_temp DESC
limit 3;
