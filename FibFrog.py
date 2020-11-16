def fib(n=25):
    # there are 26 numbers smaller than 1000
    f = [0] * (n)    
    f[1] = 1
    for i in range(2, n):
        f[i] = f[i - 1] + f[i - 2]
    print("fib - {}",f)
    return f
## projedu si zadané pole pozic updatnu si to poctem skoků na kolik nejméně se tam dá dostat ?

def solution(a):
    a.insert(0, 1)
    a.append(1)
    print("extended a{}".format(a))
    n=len(a)
    steps = [0]+[n]*(n-1)
    print ("steps {}".format(steps))

    for p in range(1, len(steps)): # position
        s_min = n

        for jump in fib(): #pro každkou pozici hledám mimnimální počet na kolik se tam dostanu
            prev_leaf = p - jump # ze kterého listu by se dalo ke skoku odrazit
            print("prev_leaf {} p {} jump {}".format(prev_leaf, p, jump ))
            if prev_leaf >= 0: # je-li případná odrazvá pozice kde může být list větší naž 0
                if a[prev_leaf] == 1 and steps[prev_leaf] + 1 < s_min: # (a[prev_leaf] == 1) je li tam  list
                #steps[prev_leaf] + 1 < s_min
                    print("s_min puv {} steps[prev_leaf] + 1 = {}".format(s_min, steps[prev_leaf] + 1 ))
                    s_min = steps[prev_leaf] + 1
            else:
                print("BREAK prev_leaf {} p {} jump {}".format(prev_leaf, p, jump ))
                break
        steps[p] = s_min
        print("steps in for ",steps)
# extended a[1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1]
# steps [0, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13]
# fib - {} [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368]
    return steps[-1] if steps[-1] != n else -1


#A=[0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0]
A= [0, 0, 0,  1, 1, 0, 1, 1, 0, 0, 0]
[0, 1, 1, 1, 13, 1, 2, 2, 1, 2, 2, 2, 3]
print(solution(A))