import os

path ='C:\\Users\\Donishal\\Desktop\\Mashupstack\\python\\Exercise'

files = []
for f in os.walk(path):
	print(f)
