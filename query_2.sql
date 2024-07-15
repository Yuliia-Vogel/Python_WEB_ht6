SELECT student_id_fk, AVG(mark) as average_mark
FROM marks
WHERE subject_id_fk = ?
GROUP BY student_id_fk
ORDER BY average_mark DESC
LIMIT 1;
