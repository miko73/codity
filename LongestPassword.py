#it has to contain only alphanumerical characters (a−z, A−Z, 0−9);
#there should be an even number of letters;
#there should be an odd number of digits.
from collections import defaultdict

def validate(S):
    res = 1
    num_alp=0
    num_dig=0
    for c in S:
        if c.isascii:
            if c.isalpha():
                num_alp +=1
            elif c.isnumeric():
                num_dig +=1
            else:
                return 0
        else:
            return 0
    if num_dig%2 == 0:
        return 0
    if num_alp%1 == 1:
        return 0
    return 1


def solution(S):
    d=defaultdict(lambda: 0)
    print(S.split())
    for str in S.split():
        d[str] = validate(str)
    max = 0
    for str in d:
        if d[str]:
            if max < len(str):
                max = len(str)
    return max

S = "test 5 a0A pass007 ?xy1"

# nacpu retězce do slovníku, budu je postupně validovat
# nejdelší z validních je výsledek.


print (solution(S))