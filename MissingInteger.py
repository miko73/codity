import sqlite3

def solution(A):
   s = {x for x in A if x > 0}
   if s:
      s = sorted(s)
   else:
      return 1
   if s[0] > 1:
      return 1

   print(s)
   for i, a in enumerate(s):
      current = a
      if i+1 < len(s):
         next = s[i+1]
      else:
         return current + 1
      print("curren {0} next {1}".format( current, next))
      if current + 1 == next: #mezera
         pass
      else:
         return current + 1
   print("last + 1 =",s[len(s)])
   return s[len(s)] + 1


A = [1,3,1,5,2,3,5,4]
A=[90, 91, 92, 93]
A = [3,2,4,3,1,5,6,7,8,9,10,11,24]
print("resolution - {0} ".format( solution(A) ) )