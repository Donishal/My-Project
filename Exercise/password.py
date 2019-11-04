import random
characters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '&', '*', '(', ')']
strength = input("Do you want a weak, medium, or strong, password?: ").lower()
new_password = []
def password(strength):
	if strength == 'weak':
		while len(new_password) != 5:
			new_password.append(characters[random.randint(1, 70)])
	elif strength == 'medium':
		while len(new_password) != 8:
			new_password.append(characters[random.randint(1, 70)])
	elif strength == 'strong':
		while len(new_password) != 14:
			new_password.append(characters[random.randint(1, 70)])
			return new_password
password(strength)
new_password = "".join(new_password)
print(new_password)

