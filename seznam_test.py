import sqlite3


def solution(A):
    A.sort()
    print (A)
    index = 0
    n_index = 1
    lowest = A[0]
    if lowest < 1:
        lowest = 1
    max=len(A)
    if A[0] > 1:
        return 1
    smallest=A[0]
    while n_index < max:
        current = A[index]
        next = A[n_index]
        #while current == next:
        #   index=index+1
        #   next=index+1
        #   if index == max:
        #     return lowest
        print("cur {0}, next {1}, return{2}", current,next, lowest)
        if next > 1 and next - current > 1: #mezera
            if current < 0:
                return 1
            else:
                return current+1

        index = index + 1
        n_index = index + 1
    if next <= 0:
            return 1

    return next + 1

#A = [4,2,3, 3, 3, 3]
#A= [1, 3, 6, 4, 1, 2]
#A=[-1, -3]
#A=[-1000000, 1000000]
A=[100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149]
#A=[90, 91, 92, 93]
#A=[1,2,3]
print (solution(A))