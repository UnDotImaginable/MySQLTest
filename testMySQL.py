import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Veer2004",
    database="testdatabase"
)

mycursor = db.cursor()

# mycursor.execute("CREATE DATABASE testdatabase")
# mycursor.execute("CREATE TABLE Frame (width smallint UNSIGNED, height smallint UNSIGNED, frameID int PRIMARY KEY AUTO_INCREMENT)")

mycursor.execute("DESCRIBE Frame")

for x in mycursor:
    print(x)
