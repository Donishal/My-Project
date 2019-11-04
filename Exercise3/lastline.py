student_file = open("student.txt","r")
lastline = student_file.readlines()
lastline= lastline[::-1]
print("Last line is", lastline[0:2])
student_file.close()