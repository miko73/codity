import sqlite3

def solution3(A):
   res = sum(A)
   for edge in range(0,len(A)-1):
      print("edge -",edge)
      left=0
      right=0
      c=0
      #left = sum(A[:edge])
      #right= sum(A[edge:])
      for a in A:
         if c <= edge:
      #     left = left + a
      #   else:
      #      right = right+a
      #   c+=1
      print("left ", A[:edge])
      print("right ", A[edge:])
      print("diff -", abs(left-right))
      print("res", res)
      if res > abs(left - right):
         res = abs(left - right)
      edge += 1
      print("=======")
   return res

def solution2(A):
   res = sum(A)
   for edge in range(1,len(A)):
      print("edge -",edge)
      left=0
      right=0
      c=0
      #left = sum(A[:edge])
      #right= sum(A[edge:])
      for a in A:
         if c <= edge:
           left += a
         else:
           right += a
         c+=1
      print("left ", A[:edge])
      print("right ", A[edge:])
      print("diff -", abs(left-right))
      print("res", res)
      if res > abs(left - right):
         res = abs(left - right)
      edge += 1
      print("=======")
   return res


def solution(a):
   l = len(a)
   ms = None  # min sum
   sl = 0  # sum left
   sr = sum(a)

   for p in range(0, l - 1):
      sl = sl + a[p]
      sr = sr - a[p]
      ab = abs(sl - sr)
      if (ms == None):
         ms = ab
      if (ms > ab):
         ms = ab
   return ms

A = [3,1,2,4,3]
print("resolution - ",solution(A))