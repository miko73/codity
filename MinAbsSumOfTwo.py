from collections import defaultdict
# (0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)
# extreme_double
# sequences of 2 elements✘WRONG ANSWER
# got 200000 expected
#     1999999998
# 1.0.036 sOK
# 2.0.036 sWRONG ANSWER, got 200000 expected 1999999998
# 3.0.036 sOK


def solution2(A):
    min_asp=200000
    for x in range(0,len(A)):
        for y in range (x, len(A)):
            #print("{} {}".format(A[x], A[y]))
            #print(abs(A[x] + A[y])
            if min_asp > abs(A[x] + A[y]):
                min_asp = abs(A[x] + A[y])
    return min_asp


def solution2(A):
    B = sorted(A)
    abs_min=2000000
    n=len(B)
    #print(B)
#y=x+1 0:1, 1:2, 2:3, 3:4
#y=x+2      1:3, 2:4
#           1:4,
#
    p=1
    q=0

    while q<n:
        for p in range(q, n):
            if p !=q:
                #print("[{}, {}] ({},{})".format(q, p, B[p], B[q]))
                if abs_min > abs(B[p] + B[q]):
                    abs_min = abs(B[p] + B[q])
        q+=1
    return abs_min

def solution3(a):
    n=len(a)

    if n==1:
        return abs(a[0]+a[0])

    a.sort()
    #print(a)

    l=0 # first
    r=n-1 # last
    m = 2000000000
    print(a)
    while l<=r:
        dif= a[l]+a[r]
        #print('dif:', dif, 'a[l]:', a[l], 'a[r]:', a[r],'l:', l, 'r:', r)
        print("{} a[{}]: {} a[{}]".format( a[l], l, a[r], r))
        if dif==0:
            return 0
        m = min(m,abs(dif))
        if dif>0:
            r=r-1
        else:
            l=l+1

    return m

def solution(a):
        #0:4 1:4, 2:4,
        #2:3,
        #2:2
    n=len(a)
    if n==1:
        return abs(a[0]+a[0])

    a.sort()
    l=0 # first
    r=n-1 # last
    m=20000000
    print(a)
    while l<=r:
        print("[{} {}]".format(l, r))
        dif= a[l]+a[r]
        #print('dif:', dif, 'a[l]:', a[l], 'a[r]:', a[r],'l:', l, 'r:', r)
        print("{} a[{}]: {} a[{}]".format( a[l], l, a[r], r))
        if dif==0:
            return 0
        m = min(m,abs(dif))
        if dif>0:
            r=r-1
        else:
            l=l+1

    return m



A=[-10, -8, 3, 4, 5]

A=[1, 4, -3]
A=[-8, 4, 5, -10, 3]
A=[-1,-2,3,4,5,6]
print(solution(A))
