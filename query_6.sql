SELECT s.first_name, s.last_name
FROM students s
JOIN group_lists g ON s.student_id_pk = g.student_id_fk
WHERE g.group_id_fk = ?;