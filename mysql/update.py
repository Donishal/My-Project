import mysql.connector
mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "",
	database = "mydatabase")
mycursor = mydb.cursor()
sql = "UPDATE student SET dept = 'Civil' WHERE ID ='4'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")
