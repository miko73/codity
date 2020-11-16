# seřadim a při změně hodnoty pojedu v county pro prvky při změnně hodnoty
# udržuji max counter domin

def solution(B):
    domin=0
    domin_val = -1
    A = sorted(B)
    print(A)
    print(B)
    for i, a in enumerate(A):
        if i == 0:
            if domin_val < A.count(a):
                domin_val = A.count(a)
                domin = i
                #print("{0} {1}".format(a, i))
        else:
            if a != A[i-1]:
                if domin_val < A.count(a):
                    domin_val = A.count(a)
                    domin = i
                    #print("{0} {1}".format(a,i))
    #print (domin)
    return domin

A=[4,3,3,2,3,-1,3,3]
print(solution(A))