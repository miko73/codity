from collections import defaultdict
#  A[P] + A[P+1] + ... + A[Q]
#(3, 4) is a slice of A that has sum 4,
#(2, 2) is a slice of A that has sum −6,
#(0, 1) is a slice of A that has sum 5,
#no other slice of A has sum greater than (0, 1).

def solution(A):
    s=set()
    P=0
    Q=0
    max=0
    for P in range(0, len(A)):
        for Q in range(0, len(A)):
            print("A[P:Q] {} sum {}".format(A[P:Q],sum(A[P:Q]) ))
            if max < sum(A[P:Q]):
                max = sum(A[P:Q])
    return max

# [0 1  2 3 4]
A=[3,2,-6,4,0]
print(solution(A))