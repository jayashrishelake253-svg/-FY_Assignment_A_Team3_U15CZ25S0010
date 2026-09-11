# Algorithm - Online Course Enrollment

START
Step 1: Create lists for Student, Course, Instructor, Enrollment
Step 2: Function AddStudent(sid, name, email) -> Add to Student list
Step 3: Function AddCourse(cid, title, desc) -> Add to Course list
Step 4: Function AddInstructor(iid, name, exp) -> Add to Instructor list
Step 5: Function Enroll(eid, sid, cid, iid)
    - Check if student exists
    - Check if course exists
    - Check if instructor exists
    - If all exist, create Enrollment with status = "Enrolled"
Step 6: Function UpdateStatus(eid, new_status)
Step 7: Display all enrollments
END
