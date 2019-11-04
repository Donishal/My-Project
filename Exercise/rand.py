import random
x=random.randrange(1,10)
y=int(input("Guess the number:"))
if x==y:
	print("Great! you guessed")
elif x>y:
	print("Tooo Big!!")
else:
	print("Tooo Low!!")


