import sqlite3

def solution(A, k):
   n = len(A)
   if (n == 0):
      return []
   res = [x for x in A]
   for y in range(1,k+1):
      s2= [x for x in res[:len(res)-1]]
      print(res)
      #print(s2)
      lastone = res[len(res)-1]
      counter=1
      for a in s2:
         res[counter] = a
         counter += 1
      res[0]=lastone
   return res


def solution_max(a, k):
   n = len(a)
   if (n == 0):
      return []
   k = k % n
   a = a[n - k:] + a[0:n - k]
   return a

A = [3, 8, 9, 7, 6]
K = 4
print(solution(A, K))
