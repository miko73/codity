def solution(N):
    s=bin(N)
    A=[]
    for ch in s:
        A.append(ch)
    A=A[2:]
    #print(A)
    gap=0
    started_gap=0
    gaps=[]
    for x in range (0, len(A)):
        #print("x {} A[x] {}".format(x, A[x]))
        if A[x] == '0':
            gap +=1
        elif A[x] == '1':
            #print("gap", gap)
            gaps.append(gap)
            gap=0
    #print(gaps)
    if len(gaps)>0:
        return max(gaps)
    return 0

N=1041
print(solution(N))