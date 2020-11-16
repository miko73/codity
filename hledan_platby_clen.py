#!/usr/bin/python

import sqlite3
import string

conn = sqlite3.connect('../db.sqlite3')
print ("Opened database successfully")
table = str.maketrans("ácčdďéeínórštúuýžÁCDÉEÍNÓRŠTÚUÝŽ\'","accddeeinorstuuyzACDEEINORSTUUYZ-")
table2 = str.maketrans("\"\'","--")


#cursor = conn.execute("SELECT id, prijmeni from moviebook_clen where id = 54")
cursor = conn.execute("SELECT id, prijmeni from moviebook_clen")
print ("pocet clenu - ", cursor.rowcount)
for row in cursor:
   print ("ID= ", row[0])
   print ("Prijmen = ", row[1])
   part_prijm = str(row[1])
   if len(part_prijm) > 5:
      if part_prijm[len(part_prijm) - 4:len(part_prijm) - 1] == 'ová':
         part_prijm = part_prijmpart_prijm[0:len(part_prijm) - 5]
      else:
         part_prijm = part_prijm[0:len(part_prijm) - 2]
   part_prijm = part_prijm.translate(table)
   select_string="select \"Protiúčet\", \"Zprávapropříjemce\",\"Poznámka\"  from vypis_komplet where"
   select_string += " upper(\"Zprávapropříjemce\") like upper(\'%"
   select_string += part_prijm
   select_string += "%\') "

   select_string += "or  upper(\"Názevprotiúčtu\") like upper(\'%"
   select_string += part_prijm
   select_string += "%\'); "



   print (select_string)

   platby = conn.execute(select_string)
   numofplateb=0
   for platba in platby:
      print("protiucet -", platba[0])
      numofplateb+=1
      print("\n")
      if numofplateb == 1:
         poznamka = str(platba[1])
         poznamka = poznamka.translate(table2)
         update_string = "update moviebook_clen set ucet_protiucet=\'"
         update_string+= str(platba[0])
         update_string += "\' "
         update_string += ", ucet_zprava_pro_prijemce = \'"
         update_string+= poznamka
         update_string += "\' "
         update_string += ", prijmeni_rodic = \'"
         update_string += str(platba[2])
         update_string += "\' "
         update_string += "where upper(prijmeni) = upper(\'"
         update_string += str(row[1])
         update_string += "\') and ucet_protiucet is NULL"
         print ("UPDATE 1 : ", update_string)
         conn.execute(update_string)
         update_string = "update moviebook_clen set ucet_protiucet2=\'"
         update_string+= str(platba[0])
         update_string += "\' "
         update_string += "where upper(prijmeni) = upper(\'"
         update_string += str(row[1])
         update_string += "\') and (ucet_protiucet is not NULL and ucet_protiucet2 is NULL)"
         print ("UPDATE 2 : ",update_string)
         conn.execute(update_string)
conn.commit()
print( "Operation done successfully")



conn.close()