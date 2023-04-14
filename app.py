from Student import Student
from Course import Course

s1 = Student("John",26,85)
s2 = Student("Bruce",27,95)
s3 = Student("Tyler",23,75)

comp_sci = Course("Computer Science",2)
comp_sci.add_student(s1)
comp_sci.add_student(s2)

# Print student details
print(comp_sci.add_student(s3))
print(comp_sci.students[0].name)
print(comp_sci.students[1].name)
print(comp_sci.get_average_grade())