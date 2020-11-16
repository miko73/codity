import sqlite3

def solution(S):
    ms = set()
    for a in S:
       ms.add(a)
    return len(ms)

S = [5,5,5,5,5,5,5]
print(solution(S))