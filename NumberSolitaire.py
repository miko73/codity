from collections import defaultdict



class Kostka:
    def __init__(self):
        self.__pocet_sten = 6

    def vrat_pocet_sten(self):
        return self.__pocet_sten
    def hod(self):
        import random as _random
        return _random.randint(1, self.__pocet_sten)



def solution(A):
    if len(A) == 1:
        return A[0]
    elif len(A)==0:
        return 0

    kostka = Kostka()
    postup=[]
    pozice=0
    sum=0
    postup.append(pozice)
    while pozice != len(A)-1:
        okolik = kostka.hod()
        if pozice+okolik <= len(A)-1:
            print("pozice {}, okolik {}".format(pozice, okolik))
            pozice += okolik
            postup.append(pozice)
            print(postup)


    for p in postup:
        print("A[{}]={}".format(p, A[p]))
        sum += A[p]

    return sum

def solution2(a):
    n=len(a)
    print(a)
    m = [a[0]]*(n + 6) # map
    print(m)
    for i in range(1, n):
        print("---------------------------------------------------------m[i:i+6], ", m[i:i+6], "max(m[i:i+6]) ", max(m[i:i+6]))
        m[i+6] = max(m[i:i+6]) + a[i]
        print ('i:',i, 'a[i]', a[i] , ' m[6:]', m[6:])

    return m[-1]

A=[1, -2, 0, 9, -1, -2]
#A=[1, -1, -2, -3, -4, -5, -6, 2]
print(solution2(A))

