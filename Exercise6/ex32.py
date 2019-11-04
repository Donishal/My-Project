import csv
with open('excel.csv','rt')as f:
  data = csv.reader(f)
  for row in data:
  		print(row[3])
  	
      
 
