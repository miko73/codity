import sqlite3

def solution(A, B, K):
    res=0
    for x in range(A,B):
        if x%K == 0:
            res+=1
            print(x)

    return res







print(solution(6,11,2))