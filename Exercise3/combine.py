with open("student.txt","r") as f , open("employee.txt","r") as f1:
	for line1,line2 in zip(f, f1):
		print(line1+line2)
