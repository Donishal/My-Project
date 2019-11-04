student_file = open("student1.txt","w")
student_file.write("lists=['a','b','c','d','e','f','g','h]")
student_file.close()

student_file = open("student1.txt","r")
print(student_file.read())
student_file.close()
