# A=[15,10,3]
# B=[75,30,5]
#return 1, because only one pair (15, 75) has the same set of prime divisors.
#nají tákladní dělitele
# vracet pocet shod
def devisor_list(a):
    div = []
    for x in range(2,a):
        if a%x==0:
            found=0
            for d in div:
                found=0
                if x%d == 0:
                   found=1
            if found == 0:
                div.append(x)

    return div


def solution(A, B):
    res=0
    div_lists=[]
    for x in range(0, len(A)):
        #print("[{}:{}]".format(A[x], B[x]))
        d1=devisor_list(A[x])
        d2=devisor_list(B[x])
        d1.sort()
        d2.sort()

        rozdilna=0
        if len(d1)==len(d2) and len(d1) >0:
            for x in range(0, len(d1)):
                if d1[x] != d2[x]:
                    rozdilna=1
        else:
            rozdilna=1

        if rozdilna == 0:
            print("A- ", d1)
            print("B- ", d2)
            res+=1

    return res


A=[15,4,200]
B=[75,8,400]


#print(semi_primes(N))

print(solution(A,B))
#print(devisor_list(75))