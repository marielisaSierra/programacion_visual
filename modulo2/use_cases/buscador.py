print("digite un nombre")
nombre = input()

print("cantidad de resultados: ","3 ")

print("{:<10} {:<10}".format("nombres", "apellidos"))

print("-"*25)
print("{:<10} {:<10}".format("albert", "garcia"))
print("{:<10} {:<10}".format("marlin", "vazquez"))
print("{:<10} {:<10}".format("aracelis", "severino"))

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="",
  password="",
  database="infotep"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE name LIKE = %s"
adr = ("%"+nombre+"%", )

mycursor.execute(sql, adr)

myresult = mycursor.fetchall()

for x in myresult:
  print(x[0])  print(x[1])