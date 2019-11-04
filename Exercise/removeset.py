num_set = {0, 1, 2, 3, 4, 5}
lists=list(num_set)
y=int(input("Enter number:"))
for x in lists:
	if x==y:
		lists.remove(x)
print(lists)