import sqlite3

#Fix this code

def solution(A):
   # initialize the bucket
   myBuckets = []
   # store number of fruits
   count = 0
   # loop for fruits in A
   for i in A:
      # if fruit not in the buckets
      if not myBuckets.__contains__(i):
         # if bucket length less than two
         if len(myBuckets) < 2:
            # add fruit in the bucket
            myBuckets.append(i)
         # else break the loop
         else: break
   count += 1
   return count


A = [1, 2, 1, 3, 4, 3, 5, 1, 2]

maxFruits = solution(A)
print(A)
print("She can collect max:", maxFruits, "fruits")

print("\n")
A = [1, 2, 1, 2, 1, 2, 1]
print(A)
maxFruits = solution(A)
print("She can collect max:", maxFruits, "fruits")