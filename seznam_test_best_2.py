def solution(A):
    N = len(A)
    count = [0] * (N + 1)
    print ("nevim - [0] * (N + 1) ", count) #created list with one extra positiion filled in with 0 like [0, 0, 0] if N = 2
    # Counts all elements of A tha belongs to sequence {1, ..., N}
    for k in range(N):
        if N >= A[k] > 0:
            count[A[k]] += 1

    # Searches for the lesser integer that not belongs to A
    for k in range(1, N + 1):
        if count[k] == 0:
            return k

    # If A has all elements from 1 to N, N + 1 is the minimal integer
    return N + 1


A=[-1, -3]
print (solution(A))