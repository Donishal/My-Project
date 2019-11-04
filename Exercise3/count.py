student_file = open("student.txt","r")
lines = len(student_file.readlines())
print(lines)
student_file.close()