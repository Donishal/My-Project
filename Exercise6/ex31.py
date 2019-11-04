import csv
with open('excel.csv','rt')as f:
  data = csv.reader(f)
  row1 = next(data) 
  print(row1)
  	
