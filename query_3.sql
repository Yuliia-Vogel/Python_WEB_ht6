SELECT g.group_id_fk, AVG(m.mark) as average_mark
FROM marks m
JOIN group_lists g ON m.student_id_fk = g.student_id_fk
WHERE m.subject_id_fk = ?
GROUP BY g.group_id_fk;
