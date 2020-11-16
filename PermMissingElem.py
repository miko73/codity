import sqlite3


def solution(A):
   A.sort()
   #print(A)
   c=0
   for x in A:
      if x+1 == A[c+1]:
         #print(x)
         pass
      else:
         return x+1
      c+=1
   return 0


def solution2(a):
   if (len(a) == 0):
      return 1
   print (max(a))
   print (len(a))
   if (max(a) == len(a)): # jen performance na úkor obecnosti
      return len(a) + 1

   a.sort()
   for _ in range(1, len(a) + 1):
      if _ != a[_ - 1]:
         return _

A = [2,3,1,5]
print("resolution - ",solution2(A))