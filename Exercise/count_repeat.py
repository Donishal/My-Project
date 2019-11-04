string= input("Enter your string:")
import collections
count = collections.Counter(string)
for letter in count:
	if count[letter]>1:
		print(letter, count[letter])

