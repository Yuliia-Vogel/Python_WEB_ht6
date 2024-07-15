SELECT AVG(m.mark) as average_mark
FROM marks m
JOIN subjects s ON m.subject_id_fk = s.subject_id_pk
WHERE s.teacher_id_fk = ?;