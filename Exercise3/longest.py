student_file = open("student.txt","r")
words = student_file.read().split()
max_len = len(max(words, key=len))
for word in words:
	if(len(word)==max_len):
		print(word)
student_file.close()