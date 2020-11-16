import sqlite3

def solution(S, P, Q):
    res=[0]*len(P)
    for x in range(0,len(P)):
#       print("[{0}:{1}]".format(P[x],Q[x]+1))
#        print(" = ",S[P[x]:Q[x]+1])
        part = S[P[x]:Q[x]+1]
        part=sorted(part)
        print(x," - ",part)
        print("[{0}:{1}]".format(P[x],Q[x]+1))
        res[x] = part[0]

    return res
S = ['2','1','4','2','2','4','1']
P = [2,5,0]
Q = [4,5,6]

print(solution(S,P,Q))