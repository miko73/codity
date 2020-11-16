#to A[Q] − A[P], provided that A[Q] ≥ A[P]. Otherwise, the transaction brings loss of A[P] − A[Q].

def solution(A):
    max = 0
    l = len(A)
    x=0
    y=0
    for x in range (0, l-1):
#        print(l -x -1)
        for y in range(x, l-1):
            print("[{} {}] max {}".format(l - x - 1, l - 2 - y, A[l - x - 1]- A[l - 2 - y]))
            if max < A[l - x - 1]- A[l - 2 - y]:
                max = A[l - x - 1]- A[l - 2 - y]
    return max
# delka bude 6
# max range 5
# pojedu 5-4,5-3, 5-2, 5-1, 5-0, 4-3, 4-2, 4-1, 4-0, 3-2, 3-1, 3-0, 2-1, 2-0, 1-0,
A=[23171,21011,21123,21366,21013,21367]

print(solution(A))