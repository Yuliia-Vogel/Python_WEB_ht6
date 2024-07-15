WITH latest_marks AS (
    SELECT m.student_id_fk, MAX(m.creation_date) as latest_date
    FROM marks m
    JOIN group_lists g ON m.student_id_fk = g.student_id_fk
    WHERE g.group_id_fk = ? AND m.subject_id_fk = ?
    GROUP BY m.student_id_fk
)
SELECT s.first_name, s.last_name, m.mark, m.creation_date
FROM students s
JOIN marks m ON s.student_id_pk = m.student_id_fk
JOIN latest_marks lm ON m.student_id_fk = lm.student_id_fk AND m.creation_date = lm.latest_date
WHERE m.subject_id_fk = ?;
