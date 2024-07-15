SELECT sub_name_u
FROM subjects
JOIN marks ON subjects.subject_id_pk = marks.subject_id_fk
WHERE marks.student_id_fk = ?;