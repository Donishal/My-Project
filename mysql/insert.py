import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO student (id, name, age, dept) VALUES (%s, %s, %s, %s)"
val =[ 
(4, "ADLIN", 21, "EEE"),
(5, "DIMALO", 20, "EEE")
]
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "row was inserted.")

