import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="mydatabase"
  )
mycursor = mydb.cursor()

sql = "INSERT INTO student(name, age, dept) VALUES (%s, %s, %s)"
sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")



