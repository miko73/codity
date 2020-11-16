import sqlite3

def solution(S):
    res = 1000000
    start = 0
    pole = S[0:len(S)]
    start_poz=-1
    while len(pole) > 1:
        start +=1
        pole = S[start:len(S)]
        for x in range(len(pole)):
            sl = pole[:x+1]
            if len(sl) > 1:
                prum = sum(sl)/len(sl)
                print("{0}-prumer :{1}".format(sl,prum))
                if res > prum:
                    res=prum
                    start_poz=start

    return start_poz

S = [4,3,5,5,1,5,8]
print(solution(S))