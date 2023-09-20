-- Lists all the cities of CA found in the database hbtn_0d_usa.
-- Results ordered in ascending order by cities.id.
SELECT id, name
  FROM cities
 WHERE state_id IN
       (SELECT id
	        FROM states
	       WHERE name = "California")
ORDER BY id;
