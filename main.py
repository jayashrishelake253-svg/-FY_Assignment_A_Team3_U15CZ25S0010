# Online Course Enrollment System - Feature Set I
# Problem 11 - Team 3 - U15CZ25S0010

class Student:
    def __init__(self, student_id, name, email):
        self.student_id = student_id
        self.name = name
        self.email = email

class Course:
    def __init__(self, course_id, title, description):
        self.course_id = course_id
        self.title = title
        self.description = description

class Instructor:
    def __init__(self, instructor_id, name, expertise):
        self.instructor_id = instructor_id
        self.name = name
        self.expertise = expertise

class Enrollment:
    def __init__(self, enrollment_id, student, course, instructor):
        self.enrollment_id = enrollment_id
        self.student = student
        self.course = course
        self.instructor = instructor
        self.status = "Enrolled"
    
    def display(self):
        print(f"Enrollment ID: {self.enrollment_id}")
        print(f"Student: {self.student.name} ({self.student.student_id})")
        print(f"Course: {self.course.title} ({self.course.course_id})")
        print(f"Instructor: {self.instructor.name}")
        print(f"Status: {self.status}")
        print("-" * 30)

# Demo Execution
if __name__ == "__main__":
    s1 = Student("U15CZ25S0010", "Jayashri", "jayashri@gmail.com")
    c1 = Course("C11", "Python Basics", "Intro to Python")
    i1 = Instructor("I01", "Prof. Sharma", "Python Expert")
    
    e1 = Enrollment("E01", s1, c1, i1)
    e1.display()
    print("Status updated to In Progress")
    e1.status = "In Progress"
    e1.display()
