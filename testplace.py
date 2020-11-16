from collections import defaultdict

def solution(A):
    x=1
    maxsum=-222222222222
    for x in range(0, len(A)):
        for y in range(x, len(A)+1):
            print(x, y)
            print("sum {}".format(sum(A[x:y])))
            if maxsum < sum(A[x:y]):
                maxsum=sum(A[x:y])
    return  maxsum


A=[3, 2, -6, 4, 0]
A=[-10]
print( solution(A) )

