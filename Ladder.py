# Například vzhledem k L = 5 a:
#
#     A [0] = 4 (4 stupinky)  B [0] = 3 (po)
#     A [1] = 4 (4 stupinky)  B [1] = 2
#     A [2] = 5 (5 stupinku)  B [2] = 4 (16)
#     A [3] = 5 (5 stupinku)  B [3] = 3 (po 8 nebo 16)
#     A [ 4] = 1 (1 stupinek) B [4] = 1 (po 2 nebo 4)
# funkce by měla vrátit sekvenci [5, 1, 8, 0, 1], jak je vysvětleno výše.

def fib(n=50):
    # there are 26 numbers smaller than 100k
    f = [0] * (n)
    f[1] = 1
    for i in range(2, n):
        f[i] = f[i - 1] + f[i - 2]

    return f

f = fib(n=50)[1:]


def step2(n=30):
    s = [0]*n
    for i in range(1, n):
        s[i]=2**i
    return s

s = step2()

def solution(a,b):
    print("fib f {}".format(f))
    print("step2 s {}".format(s))
    n = len(a)
    r = [0]*n

    for i in range(0,n):
        print("a[i] = {} | f[a[i]] = {} | b[i] = {} | s[b[i]] = {}".format(a[i], f[a[i]], b[i], s[b[i]] ))
        r[i]=f[a[i]] % s[b[i]]
    return r




A= [4, 4, 5, 5, 1]
B= [1, 2, 4, 3, 1]
print(solution(A, B))
#print( 10 % 3)