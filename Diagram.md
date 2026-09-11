# ER Diagram - Online Course Enrollment

Tables:
Student (student_id PK, name, email)
Course (course_id PK, title, description)
Instructor (instructor_id PK, name, expertise)
Enrollment (enrollment_id PK, student_id FK, course_id FK, instructor_id FK, status)

Relation:
Student 1 --- Many Enrollment
Course 1 --- Many Enrollment
Instructor 1 --- Many Enrollment
