import sqlite3


def solution2(x, a):
   l = len(a)
   s = set()
   r = -1  # return
   for i, e in enumerate(a):
      s.add(e)
      print("{0} - {1} /len {2}".format(i, e, len(s)))
      if (len(s) == x):
         return i
   return -1

def solution3(x,A):
   e = -1
   steps={0,0}
   path = set()
   for e, a in enumerate(A):
      if a < x:
         if a in path:
            path[a] = path[a] + 1
         else:
            path.add(a)
            path[a] = 1
      elif a==x:
         if path.__and__(path):
            return e
   return e

def solution(x,A):
   l = len(A)
   r = -1
   path=set()
   for i, a in enumerate(A):
      path.add(a)
      #print("{0} - {1}".format(i,a))
      if a == x:
         if len(path) == x-1:
            return i
   return r


A = [1,3,1,5,2,3,5,4]
A = [1,3,1,3,4,2,5,4]
print("resolution - {0} - {1}".format(solution(5,A),solution2(5,A)))

