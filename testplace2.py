from functools import reduce

def solution(S):
    #print(S)
    lower=dict()
    upper=dict()
    f_count=0
    fragments=[]
    unbalanced_string=""
    for s in S:
        if s.islower():
            #print("s is loww", s)
            if S.find(s.upper())>=0:
                pass
            else:
                #print("neni tam{}", s.upper())
                unbalanced_string+=s # neni tam upper.
        elif s.isupper():
            #print("s is upper", s)
            if S.find(s.lower())>=0:
                pass
            else:
                #print("neni tam{}", s.lower())
                unbalanced_string+=s  # neni tam low.
    max_balanced=[]
    counter=0

    for s in range(0,len(S)):
        #print(unbalanced_string.find(S[s]))
        if unbalanced_string.find(S[s]) >= 0:
            print("s {} S[s] {}".format(s, S[s]))
            max_balanced.append(counter)
            counter=0
        else:
            counter+=1
        #print(max_balanced)
    max_balanced.append(counter)
    if len(max_balanced) > 0:
        if max(max_balanced) > 1:
            return max(max_balanced)
        else:
            return  -1
    else:
        return -1

S="azABaabza"
S="TacoCat"
S="AcZCbaBz"
print(solution(S))