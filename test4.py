import sqlite3
conn = sqlite3.connect('../db.sqlite3')
print ("Opene database successfully")


cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("SALARY = ", row[3])
   print ("\n")
print( "Operation done successfully")
conn.close()