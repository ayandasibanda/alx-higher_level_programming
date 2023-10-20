-- Lists all records of the table second_table that have a name value.
-- The records are ordered by descending score.
SELECT score, name
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC;
