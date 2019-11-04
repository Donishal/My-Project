from collections import Counter
student_file = open("student.txt","r")
x = student_file.read().split()
print("Number of words in the file:", Counter(x))