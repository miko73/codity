from collections import defaultdict
#A=[10, 2, 5, 1 , 8, 12]
#(0, 2, 4), (0, 2, 5), (0, 4, 5), and (2, 4, 5).
# seřadit
#[12, 10, 8, 5, 2, 1]
def solution(A): #63
    A.sort()
    print(A)
    n=len(A)
    c=0
    triangels=set()
    for p in range(0, n-2):
        q=p+1
        r=p+2
        while q < n-1 :

            while r<n:
                if (A[p] + A[q] > A[r]) and (A[r] + A[q] > A[p]) and (A[p] + A[r] > A[q]) :#trojuhelnik
                   # print("p {}, q {}, r {}, c {}".format(p, q, r, c))
                    c+=1
                    triangels.add("{},{},{}".format(A[p],A[q],A[r]))
                    print(triangels)
                r+=1
            q+=1
            r=q+1
    print(triangels)
    return len(triangels)


def solution(a):
    n=len(a)
    a.sort()
    print(a)
    c=0
    for p in range(0, n-2):
        q=p+1
        r=p+2
        while r<n:
            print("{}, {}, {}|c={}".format(a[p], a[q], a[r], c))
            if a[p]+a[q]>a[r]:
                c+=r-q
                r+=1
            elif q<r-1:
                q+=1
            else:
                r+=1
                q+=1
    return c

def solution2(B):
    A = sorted(B,reverse=True)
    res=0
    for x in range(0, len(A)):
        for y in range(x+1, len(A)):
            for z in range(y+1, len(A)):
                if A[x] < A[y] + A[z]:
                    #print("({},{},{})=({},{},{})".format(x, y, z, A[x], A[y], A[z]))
                    res +=1
    return res

B=[10, 2, 5, 1 , 8, 12]
print(solution(B))
