n=int(input("Enter a number:"))
print("The divisor of the number is:")
for i in range(1,n+1):
	if(n%i==0):
		print(i)