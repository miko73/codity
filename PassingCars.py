import sqlite3

def solution(a):
    pc = 0
    fz = 0

    for e in a:
        if pc > 1000000000:
            return -1
        if e == 0:
            fz += 1
        else:
            pc += fz
        print("[{} - {}]".format(fz, pc))
    return pc
A = [1,1,1,1,1]
A = [0,1,0,1,1]

print(solution(A))