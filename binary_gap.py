import sqlite3
#1) prevod in na bin
n = 2000000000
#  b=bin(n)[2:]
b=bin(n)
c = b[2:len(b)]
print(b)
print(c)
#2) rozbor bin retezce
nul_max=[]
prev=1
current=1
ukonceno=1
for x in c:
   prev = current
   current = x
   if prev == "1" and current == "0":
      ukonceno = 0
      nul_max.append(1)
   elif prev == "0" and current == "0":
      nul_max[len(nul_max)-1] += 1
   elif prev == "0" and current == "1":
      ukonceno = 1
if ukonceno:
   pass
else:
   nul_max[len(nul_max) - 1] = 0
   ukonceno = 0

nul_max.sort()
if nul_max:
   print(nul_max[len(nul_max)-1])
else:
   print("no gaps")

