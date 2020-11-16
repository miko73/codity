from collections import defaultdict
# A[X + 1] + A[X + 2] + ... + A[Y − 1] + A[Y + 1] + A[Y + 2] + ... + A[Z − 1].
# double slice (0, 3, 6), sum is 2 + 6 + 4 + 5 = 17,
# double slice (0, 3, 7), sum is 2 + 6 + 4 + 5 − 1 = 16,
# double slice (3, 4, 5), sum is 0.
#   0 1 2  3 4 5  6 7
#A=[3,2,6,-1,4,5,-1,2]


def solution(A):
    s=set()
    X=0
    Z=0
    max=0
    for X in range(0, len(A)):
        for Z in range(0, len(A)):
            for Y in range(X+1, Z-1):
                    #print("[{} {} {} ] - {}".format(X,Y,Z,sum(A[X+1:Y-1]) + sum(A[Y+1:Z-1]) ))
                    m = sum(A[X+1:Y]) + sum(A[Y+1:Z])
                    print("[{} {} {} ] - {} + {} = {}".format(X, Y, Z, A[X + 1:Y], A[Y + 1:Z], m))
                    #print("m {} max {}".format(m, max))
                    if max < m:
                        max = m
    return max

def solution2(a):
    n = len(a)
    k1=[0]*n
    k2=[0]*n
    for i in range (1, n):
        k1[i] = max(k1[i-1] + a[i], 0)
    for i in range (n-2, 0, -1):
        k2[i] = max(k2[i+1] + a[i], 0)
    m=0 # max
    for i in range(1, n-1):
        m = max(m, k1[i-1]+k2[i+1])
    return m

A=[3,2,6,-1,4,5,-1,2]

print(solution(A))