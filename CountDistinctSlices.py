import sqlite3
#(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2), (3, 3), (3, 4) and (4, 4).

def solution1(M, A):
    slices=set()
    res=0
    if len(A)==0:
        return 0

    for x in range(0, len(A) ):
        for y in range(x, len(A) ):
            print("[{}:{}] = {}".format(x,y, A[x:y+1]))
            s=set()
            for a in A[x:y+1]:
                s.add(a)
            if len(s) == len(A[x:y+1]):
                #print("do res", s)
                res+=1
    return res

def solution2(m, a):
    n = len(a)
    m = max(a)
    c = 0
    mask = [0]*(m+1)
    print(a)
    print(mask)

    l,r=0,0 # left and right slice indices
    while (l<=r< n):
        while (r < n and mask[a[r]] != 1):
            c += (r-l+1)
            mask[a[r]] = 1
            r += 1
            print("lefrt {} right {} mask{} ".format(l,r,mask, c))
        else:
            while r < n and l < n and a[l] != a[r]:
                mask[a[l]] = 0
                l += 1
            mask[a[l]] = 0
            l += 1
            print(l,r,mask, c)
    return min(c, 1000000000)

def solution(m,a):
    n = len(a)
    m = max(a)
    c=0 #counter
    print(a)
    for i in range(0,n):
        j=i
        while len( set( a[i:j+1] ) ) == j-i+1:
            print("j {} i {} a[i:j+1] {} c {}".format(j,i,a[i:j+1],c))
            c+=1
            j=j+1
    return c

A = [3,4,5,5,2]

print(solution(6,A))