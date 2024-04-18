import pymysql

dataBase = pymysql.connect(
  host="localhost",
  user="root",
  password="et957313"
)

cursorObject = dataBase.cursor()

cursorObject.execute('CREATE DATABASE IF NOT EXISTS db_whole')

print('Database created successfully')

