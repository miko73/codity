import sqlite3


def solution(N,A):
    matice=[]
    max = 1
    temp_rada=[]
    #if 1 <= A[0] <= N:
    for a in A:
        rada=[]
        if len(temp_rada) > 0:
            for z in temp_rada:
                rada.append(z)
        else:
            for i in range(0, N):
                rada.append(0)
        if 1 <= a <= N:     #zvyseni
            rada[a-1] += 1
            if rada[a-1] > max:
                max = rada[a-1]
            #print("1 - ", rada, a)
        elif a == N+1:      #max counter
            for u in range(0,len(rada)):
                rada[u]=max
        #print("1 - ", matice, a)
        matice.append(rada)
        temp_rada = []
        for z in rada :
            temp_rada.append(z)

    for c in matice:
        print(c)

A = [3,4,4,6,1,4,4]
N = 5
print(solution(N, A))


