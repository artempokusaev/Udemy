# Эта программа читает файл json и загоняет в БД MySQL данные

import json
import mysql.connector

con = mysql.connector.connect(
    user = "root",
    password = "123456",
    host = "localhost",
    database = "testdb"
)
cursor = con.cursor()

# читаю данные из json файла
jsondata = json.load(open("app1/teaching/data.json"))

for word in jsondata.items():
    sql = "INSERT INTO dictionary(Expression, Definition) VALUES(%s, %s)"
    expression = word[0]
    definition = word[1][0]
    val = (expression, definition)
    cursor.execute(sql, val)
    #print(val + " - " + val2)
con.commit()

