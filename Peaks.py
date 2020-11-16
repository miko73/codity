from collections import defaultdict
# pojedu polem a určím vrcholy
#
#prvni neni vrchol
#posledni neni vrchol
#jak rozdělit pole kolem vrcholů
# projedu pole, najdu vrcholy
# je-li vzdálenost vrcholů jedna, ukončíme skupinu hned za prním vrcholem
#skupina bez vrcholu musí být připojena zpět k poslední skupině s vcholem
# rozdělím to na jednotlivá pole
#udělám dic pozic a ke keždé z  nich co ta pozice znamená, příznamky First, Last, Peak
#len=12
#last index = 11
#A=[1,2,3, 4 ,3, 4 ,1,2,3,4, 6 ,2]

def solution(A):
    d = defaultdict(lambda :0)
    is_first=1
    is_last=0
    res =0
    from_peek = 0
    for x in range(0, len(A)) :
        if x == len(A)-1:
            d[x] = "plain"
        else:
            if is_first:
                d[x] = "first"
                is_first = 0
            elif A[x-1] < A[x] and A[x] > A[x+1]:
                if from_peek > 0:
                    d[x] = "peak"
                    from_peek = 0
            else:
                d[x] = "plain"
        from_peek+=1
    l_index = len(d) -1
    last_element=""
    for el in d:
        print(el,d[el])
        if d[el] == "peak":
            res +=1
    return res


A=[1,2,3,4,3,4,1,2,3,4,6,2]
print(solution(A))