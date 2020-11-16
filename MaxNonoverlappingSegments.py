from collections import defaultdict
#vratit pocet neprekrytych segmentu

def solution(a,b):
    l = len(A)
    cnt=1
    end=B[0]
    for x in range(0, l):
        print("[{}:{}]".format(A[x], B[x]))
        if A[x] > end:
            print("added")
            cnt +=1
            end = B[x]

    return cnt



A=[1, 3, 7, 10, 13, 6]
B=[5, 6, 8, 11, 13, 14]
A=[1, 3, 7, 9, 9]
B=[5, 6, 8, 9, 10]

print(solution(A, B))

