import os
import datetime

path ='C:\\Users\\Donishal\\Desktop\\Mashupstack\\python\\Exercise6'

files = []
for f in os.listdir(path):
	if '.txt' in f:
		x=f[2:4]
		x=int(x)
		y=datetime.datetime(2017,x,6)
		z=y.strftime("%b")
		print(z+ "-" +f)
