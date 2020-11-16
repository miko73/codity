from collections import defaultdict
# svazat lana tak zby vznikolo co nejvice lan delky vetsi nebo rovno K {4}
# vyřadim a započtu všechny lana větší a rovno K
def solution(k,a):
    an = [e if e<k else 0 for e in a]
    print("an ", an)
    gek = 0
    for e in an:
        if e==0:
            gek+=1

    ts=0
    for e in an:
        if e==0:
            ts=0
        else:
            ts+=e
            print("{} {}".format(ts, e))
            if ts>=k:
                gek+=1
                ts=0
    return gek



A=[1, 1, 1, 1, 2, 3, 4, 3, 3, 3, 3, 1, 1, 3]
K=4
print(solution(K,A))
