
#   val(A, S) = |sum{ A[i]*S[i] for i = 0..N−1 }|
# looking for array, which will make A as small as possible, like S = [−1, 1, −1, 1]
def calc_it(A, B, z, val):
    sum=0
    for x in range(0, len(A)-1):
        sum+= A[x]*B[x]
    return sum

def solution(A):
    A.sort(reverse=True)
    l=0
    r=len(A)-1
    B=[1]*len(A)
    if r <= 0:
        return 0

    for x in range(0, r):
        cur = calc_it(A, B, )







        print("l[{}] {}, r[{}] {}".format(l, A[l], r, A[r] ))



    return res

def golden_min_abs_sum(A):
    N = len(A)
    M = 0
    for i in range(N):
        A[i] = abs(A[i])
        M = max(A[i], M)
    S = sum(A)
    print("S", S)
    count = [0] * (M + 1)
    print("M ", M)
    for i in range(N): #
        count[A[i]] += 1
        #print("count[A[i]] {}, A[i] {}, i {}".format(count[A[i]], A[i], i))
    print("count - ", count)
    #count -  [0, 1, 2, 0, 0, 1] 0x0, 1x1, 2x2, 0x3, 0x4, 1x5 (pocty hodnot=cetnost hodnot v poly A o 0 do max hodnty)
    dp = [-1] * (S + 1) #vytvori pole hodnot -1 o velikosti sum(A)+1
    dp[0] = 0 # zacne 0
    print("dp", dp)

    for a in range(1, M + 1): #a od 1 do 6
        if count[a] > 0: #pro jednotlivé hodnoty v poly A když tam jsou
            for j in range(S): #projede pole dp
                print("j {0}, dp[{0}] {1}, a {2}, count[{2}] {3}".format(j , dp[j] , a , count[a]))
                if dp[j] >= 0:
                    dp[j] = count[a]
                elif (j >= a and dp[j - a] > 0):
                    dp[j] = dp[j - a] - 1
    print("dp po cyklu ", dp)
    #dp obsahuje
    result = S
    for i in range(S // 2 + 1):
        if dp[i] >= 0:
            result = min(result, S - 2 * i)

    return result

def solution27(a):
    n=len(a)
    ms=0
    s=0
    for i in range (0,n):
        if ms>0:
            s=-1
        else:
            s=1

        if a[i]<0:
            s=-s
        ms+=s*a[i]
        print("i {0}, ms {1}, s {2}, a[{0}] {3}".format(i , ms , s , a[i]))
    return abs(ms)

def solution(A):
    n=len(A)
    soucet=0
    for x in range(0, n):
        print(A[x])
        if soucet > 0:
            s = -1
        else:
            s = 1

        if A[x] < 0:
            s = -s
        soucet += A[x] * s
    return abs(soucet)


A=[ 1, 5, 2,-2]
# [-2, 1, 2, 5]
# [5, 2, 1, -2]


print(solution(A))
#print(golden_min_abs_sum(A))


