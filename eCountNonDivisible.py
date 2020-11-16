#A=[3,1,2,3,6]

#A[0] = 3, the non-divisors are: 2, 6,
#A[1] = 1, the non-divisors are: 3, 2, 3, 6,
#A[2] = 2, the non-divisors are: 3, 3, 6,
#A[3] = 3, the non-divisors are: 2, 6,
#A[4] = 6, there aren't any non-divisors.
#A=[3,1,2,3,6]
# najdi neděliče return [2, 4, 3, 2, 0]
# udělám si pole res o stenem poctu prvku
# vezmu prvek a projedu s ním zbytek, kdyz najdu do res[i] +=1
# return res


def solution(A):
    res=[0]*len(A)
    for x in range(0, len(A)):
        for y in range(0, len(A)):
#            if x==1: print (A[x],A[y])
            if A[x]%A[y]>0:
                res[x] += 1
    return res


A=[3,1,2,3,6]

#print(semi_primes(N))
print(solution(A))