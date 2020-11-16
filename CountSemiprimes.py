from collections import defaultdict
#jsou primes 2, 3, 5, 7, 11 and 13.
#semiprimes jsou 4, 6, 9, 10, 14, 15, 21, 22, 25, 26 ruzne dělitele ale puze dva
#PQ jsou dve pole semiprimes
#(P[K], Q[K]), where 1 ≤ P[K] ≤ Q[K] ≤ N.
#The number of semiprimes within each of these ranges is as follows:
#P=[1,4,16]
#Q=[26,10,20]
#N=26
#12 = 2x6 ale taky 3x4


#(1, 26) is 10, (4, 6, 9, 10, 14, 15, 21, 22, 25, 26)
#(4, 10) is 4,  (4, 6, 9, 10)
#(16, 20) is 0. ()
# should return array [10,4,0]
#jak najdu semiprimes
# pak je nacountuju po výsečích.

def solution(P,Q,N):
    semi=[]
    for x in range(2, N+1):
        poc = 1
        for y in range(2,x):
            #if x ==8: print("{}|{}".format(x,y))
            if x%y == 0:
                if x//y==y:
                    poc+=2
                else:
                    if semi.count(x//y)>0:
                        print("tady", x//y)
                        poc += 2
                    else:
                        poc+=1
            if poc > 2:
                break

        if poc==2:
            semi.append(x)
        #print("[{} | {}]".format(x,poc))



    semi=[4, 6, 9, 10, 14, 15, 21, 22, 25, 26]
    print(semi)

    res=[0]*len(P)
    for x in range(0,len(P)):
        print("[{}:{}]".format(P[x], Q[x]+1))
        temp=[x for x in range( P[x], Q[x]+1)]
        print(temp)
        for y in temp:
            if semi.count(y):
                print(y)
                res[x]+=1

    return res


P=[1,4,16]
Q=[26,10,20]
N=26
#print(semi_primes(N))

print(solution(P,Q,N))