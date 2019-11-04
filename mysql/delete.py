import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "DELETE FROM student WHERE id = ''"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "records deleted")
