#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('../db.sqlite3')
print ("Opened database successfully")

cursor = conn.execute("SELECT Jmeno, prijmeni, rodne_cislo, datum_narozeni, sportovcem_od from FO_zakladna_2019_uni")
for row in cursor:
   print ("Jmeno = ", row[0])
   print ("Prijmen = ", row[1])
   print ("RC = ", row[2])
   print ("datum narozeni = ", row[3])
   print ("sportovcem od = ", row[4])
   insert_string = "INSERT INTO moviebook_clen (jmeno, prijmeni, rc, narozen, clenem_od, active) VALUES ("
   insert_string += " '" + str(row[0]) + "' "
   insert_string += ", '" + str(row[1]) + "' "
   insert_string += ", '" + str(row[2]) + "' "
   insert_string += ", '" + str(row[3]) + "' "
   insert_string += ", '" + str(row[4]) + "' "
   insert_string += ", 1)"
   print(insert_string)
   print ("\n")
   conn.execute(insert_string)

conn.commit()
print( "Operation done successfully")



conn.close()