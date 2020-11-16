import sqlite3
#fine the unique
def solution(A):
    existing = []
    for a in A:
        if A.count(a) > 1:
            pass
        else:
            existing.append(a)

    return existing


A = [1,1,2,3,2,3,3,4,4,5]
print(solution(A))