# Requirements - Feature Set I
### Problem 11: Online Course - Course Enrollment

Functional Requirements:
1. Student details - Add/View student with id, name, email
2. Course details - Add/View course with id, title, description
3. Instructor - Add/View instructor with id, name, expertise
4. Enrollment - Enroll a student to a course under an instructor
5. Enrollment Status - Track status like Enrolled, In Progress, Completed

Entities:
- Student: student_id, name, email
- Course: course_id, title, description
- Instructor: instructor_id, name, expertise
- Enrollment: enrollment_id, student_id, course_id, instructor_id, date, status
