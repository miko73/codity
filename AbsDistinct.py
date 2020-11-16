import sqlite3

def solution(A):
    s = set()
    for a in A:
        a = a.__abs__()
        s.add(a)
        #print(s)
    return len(s)


A = [-5, -3, -1, 0, 3, 6]

print(solution(A))