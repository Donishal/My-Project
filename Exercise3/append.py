student_file = open("student.txt","a")
student_file.write("\nThasneem - Civil Engg")
student_file.close()

student_file =open("student.txt","r")
print(student_file.read())
student_file.close()
