import mysql.connector

con = mysql.connector.connect(
    user = "root",
    password = "123456",
    host = "127.0.0.1",
    database = "testdb"
)

cursor = con.cursor()
sql = "INSERT INTO dictionary (Expression, Definition) VALUES (%s, %s)"
val = ("My expression3", "My value3")
cursor.execute(sql, val)
con.commit()
query_select = cursor.execute("SELECT * FROM dictionary")
result = cursor.fetchall()

print(result)