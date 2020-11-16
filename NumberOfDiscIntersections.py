import sqlite3
def solution(A):
    posun = 0
    delka = len(A)
    e = []
    for i, a in enumerate(S):
        e += [(i-a,1),(i+a,0)] #nauklada is zacatky kruhu na ose (1) a konce kruhu na ose (0) do pole e
        #print(i-a, i, i+a)
    print(e)
    e.sort(key=lambda x: (x[0], not x[1])) #pole e sesortuje podle pruniku kruhu s osou
    print(e)
    c=0 # count of intersections
    ac=0 # active circles

    for _, start in e: #jedeme kruhy jeden za druhym a bereme is priznak startu nebo konce.
    #    print("start = {0} c = {1} ac = {2}".format( start, c, ac))
        if start:
            c+=ac #k celkovemu poctu pruniku, pricte pocet probihajicich kruhu
            ac+= 1 # pocet probihajicich kruhu ++
        else:
            ac-= 1 #jestlize nejaky kruh konci snizi se pocet aktivnich kruhu
        if c > 10000000:
            return -1
    return c

S = [1,5,2,1,4,0]
solution(S)