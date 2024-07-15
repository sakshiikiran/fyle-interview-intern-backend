-- Write query to find the number of grade A's given by the teacher who has graded the most assignments
WITH TeacherMaxAAssignments AS (
    SELECT teacher_id, COUNT(*) AS num_a_assignments
    FROM assignments
    WHERE grade = 'A'
    GROUP BY teacher_id
    HAVING COUNT(*) = (
        SELECT MAX(num_a_assignments)
        FROM (
            SELECT COUNT(*) AS num_a_assignments
            FROM assignments
            WHERE grade = 'A'
            GROUP BY teacher_id
        ) AS max_a_assignments
    )
)

SELECT t.teacher_id, t.num_a_assignments
FROM TeacherMaxAAssignments t;
