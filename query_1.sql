SELECT student_id_fk, AVG(mark) as average_mark
FROM marks
GROUP BY student_id_fk
ORDER BY average_mark DESC
LIMIT 5;
