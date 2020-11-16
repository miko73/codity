#!/usr/bin/python

import sqlite3
import string

conn = sqlite3.connect('../db.sqlite3')
print ("Opened database successfully")
table = str.maketrans("ácdéeěínórštúuýžÁCDÉEÍNÓRŠTÚUÝŽ","acdeeeinorstuuyzACDEEINORSTUUYZ")

cursor = conn.execute("SELECT id, prijmeni from moviebook_clen")
for row in cursor:
   print ("ID= ", row[0])
   print ("Prijmen = ", row[1])
   part_prijm = str(row[1])
   if part_prijm[len(part_prijm)-4:len(part_prijm)-1] == 'ová':
      part_prijm = part_prijmpart_prijm[0:len(part_prijm)-5]
   else:
      part_prijm = part_prijm[0:len(part_prijm) -2]
   select_string="select \"E-mail1-Value\" from contacts where upper(\"E-mail1-Value\") like upper(\'%"
   select_string += str(part_prijm).translate(table)
   select_string += "%\');"
   print (select_string)
   emails = conn.execute(select_string)
   numofmails=0
   for sep_mail in emails:
      print("emails -", sep_mail[0])
      numofmails+=1
      print("\n")
   if numofmails == 1:
      update_string="update moviebook_clen set email=\'"
      update_string+=sep_mail[0]
      update_string += "\' where upper(prijmeni) = upper(\'"
      update_string += str(row[1])
      update_string += "\')"
      print (update_string)
      #conn.execute(update_string)

conn.commit()
print( "Operation done successfully")



conn.close()