import sqlite3

def solution(A):
    s = {x for x in A if x > 0}
    if not s:
        return 1
    last = max(s)+1
    print ("s - ", s)
    # Find elements present in either of the two sets, but not common to both the sets
    s2 = set(range(1, last))
    print ("s2 od 1 do max - ",s2)
    #new_set = s2.intersection(s)
    new_set = s2.difference(s)
    #new_set = s^set(range(1, last))
    print("prunik? - ", new_set)

    if not new_set:
        return last

    return min(new_set)

#A = [4,2,3, 3, 3, 3]
#A= [1, 3, 6, 4, 1, 2]
#A=[-1, -3]
#A=[-1000000, 1000000]
#A=[100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149]
#A=[90, 91, 92, 93]
#A=[1,2,3]
A=[1,2,3, 5, 99, 199]
print (solution(A))