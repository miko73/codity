 # N = 10 and M = 4. You will eat the following chocolates: 0, 4, 8, 2, 6.
 # dám to dictu 0 az N
 # pak pojedu cyklem se skokem M, prepnu snědené na snědené

def my_solution(N,M):
    peaces=[0]*N
    snedena=0
    peaces[0] = 1
    p_i=0
    counter=4
    ret=1
    while snedena==0:
        p_i += 1
        if p_i == len(peaces):
            p_i = 0

        counter -= 1
        print("p_i {} counter {}".format(p_i, counter))
        if counter==0:
            if peaces[p_i] == 1:
                snedena=1
            else:
                peaces[p_i]=1
                ret += 1
            counter=4
    return ret

def gcdm(a, b):
    if a % b == 0:
        return b
    else:
        return gcdm(b, a % b)

def solution(n, m):
    m = m%n
    if(m==0):
        return 1
    else:
        return int(n/gcdm(n,m))


N=10
M=4
print(solution(N, M))