with open("student.txt") as f:
	with open("student2.txt","w") as f1:
		for line in f:
			f1.write(line)
f.close()
f1.close()


