from collections import defaultdict

def solution2(A):
    first_d=defaultdict(lambda :0)
    sec_d=defaultdict(lambda :0)
    leader=0
    for i, a in enumerate(A):
        #print("{} {}".format(i, len(A)//2))
        if i < len(A)//2:
            first_d[a] += 1
        else:
            sec_d[a] += 1

    print(first_d.items())
    print(sec_d.items())

    max=0
    for x in first_d:
        if max < first_d[x]:
            max = first_d[x]

    print(max, len(A) / 4)
    if max > len(A)/4:
        leader+=1

    max = 0
    for x in sec_d:
        if max<sec_d[x]:
            max = sec_d[x]
    print(max, len(A)/4)
    if max > len(A)/4:
        leader+=1

    return leader


def leader(a):
    n = len(a)
    if (n == 0):
        return None
    if (n == 1):
        return a[0]
    if (n == 2 and a[0] == a[1]):
        return a[0]

    d = sorted(a)[n // 2]
    dn = 0
    for e in a:
        if e == d:
            dn += 1
    if dn > n // 2:
        return d
    else:
        return None


def solution(a):
    n = len(a)
    l = leader(a)

    if None == l:
        return 0
    if 1 == n:
        return 0
    if 2 == n:
        return 1

    cnt = 0

    dl, dr = {}, {}
    for i in range(n):  # init dr
        if a[i] not in dr:
            dr[a[i]] = 1
        else:
            dr[a[i]] += 1
    ld = a[0]  # leader

    for i in range(n):
        if a[i] not in dl:
            dl[a[i]] = 1
        else:
            dl[a[i]] += 1

        dr[a[i]] -= 1

        if dl[ld] < dl[a[i]]:
            ld = a[i]  # new leader from dl

        if (i + 1) // 2 < dl[ld] and (n - (i + 1)) // 2 < dr[ld]:
            cnt += 1
    return cnt


A=[4, 3, 4, 4, 4, 2]
print(solution(A))