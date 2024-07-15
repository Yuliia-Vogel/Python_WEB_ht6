SELECT s.first_name, s.last_name, m.mark
FROM students s
JOIN marks m ON s.student_id_pk = m.student_id_fk
JOIN group_lists g ON s.student_id_pk = g.student_id_fk
WHERE g.group_id_fk = ? AND m.subject_id_fk = ?;