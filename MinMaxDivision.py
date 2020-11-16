import sqlite3
from collections import defaultdict

# K casti

# M maximalni hodnota v poli A
# A je pole
# K = 3, M = 5
#  0  1  2  3  4  5  6
# [2], [1, 5, 1, 2], [2, 2] with a large sum of 9;
# [2, 1], [5, 1], [2, 2, 2] with a large sum of 6.
# [2, 1, 5], [1, 2],[ 2, 2] with a large sum of 8;
# [2, 1, 5, 1], [2, 2], [2] with a large sum of 9;
# [2, 1, 5, 1, 2, 2, 2], [], [] with a large sum of 15;
# A = [2, 1, 5, 1, 2, 2, 2]
# rozdělit na K přibližně stejně velké části
# spocitat sumy,
# naít tu největší,
# největší zmenšovat s ostatní zvětšovat
#   dokud nebude suma první rovna dalším,
#   nebo velikost 1
def get_max_sector(A, K):
    max_s = 0
    max_index=0
    for x in range(0,K):
        if sum(A[x])>max_s:
            max_s=sum(A[x])
            max_index=x
    return max_index


def solution(K,M,A):
    l=len(A)
    pocet_prvku = l
    s_init=l//K #init velikost sektoru
    sektory=[]
    pozice=0
    max_sector = 0
    sum_max = 0
    min_sum_in_sector= sorted(A)[-1]
    for x in range(0,K):
        if x != K-1:
            sektory.append(A[pozice:pozice+s_init])
        else:
            sektory.append(A[pozice:])
        pozice +=s_init
        if sum(sektory[x]) > sum_max:
            sum_max = sum(sektory[x])
            max_sector = x
    #print("At the start ",sektory)
    # ma soused vic ? vezmi si jeho jeden
    stop_it=0
    while stop_it == 0:
        if max_sector == len(sektory)-1: #je posledni
            #move prvek back
            if sum(sektory[max_sector-1])+ sektory[max_sector][0] <= sum(sektory[max_sector]):
                sektory[max_sector-1].append(sektory[max_sector][0])
                sektory[max_sector] = sektory[max_sector][1:]
            else:
                #print("u posledniho to se nevyplati")
                stop_it = 1
            # reclaculate
            #print("in last",sektory)
        elif max_sector == 0: # je prvni
            if sum(sektory[max_sector+1])+sektory[max_sector][-1] < sum(sektory[max_sector]) :
                sektory[max_sector+1].insert(0,sektory[max_sector][-1])
                sektory[max_sector]= sektory[max_sector][:len(sektory[max_sector]) -1]
                #print("in firs",sektory)
            else:
                #print ("in the first to se nevyplati")
                stop_it = 1
        else: # je uvnitř
            if sum(sektory[max_sector+1]) > sum(sektory[max_sector -1]): #je -li sektor vpravo menší než ten vlevo
                if sum(sektory[max_sector-1])+ sektory[max_sector][0] <= sum(sektory[max_sector][1:]):
                    sektory[max_sector-1].append(sektory[max_sector][0])
                    sektory[max_sector] = sektory[max_sector][1:]
                else:
                    #print("in middle left < right to se nevyplati")
                    stop_it = 1
                # reclaculate
                #print("in middle move to left",sektory)
            elif sum(sektory[max_sector+1]) < sum(sektory[max_sector-1]):
                if sum(sektory[max_sector+1])+sektory[max_sector][-1] < sum(sektory[max_sector]):
                    sektory[max_sector+1].insert(0,sektory[max_sector][-1])
                    sektory[max_sector]= sektory[max_sector][:len(sektory[max_sector]) -1]
                else:
                    #print ("in middle right > left to se nevyplati")
                    stop_it = 1
            else:
                if sektory[max_sector][0] > sektory[max_sector][-1]:
                    if sum(sektory[max_sector+1])+sektory[max_sector][-1] < sum(sektory[max_sector]):
                        sektory[max_sector+1].insert(0,sektory[max_sector][-1])
                        sektory[max_sector]= sektory[max_sector][:len(sektory[max_sector]) -1]
                    else:
                        #print ("in middle right = left move to right to se nevyplati")
                        stop_it = 1
                else:
                    if sum(sektory[max_sector-1])+ sektory[max_sector][0] <= sum(sektory[max_sector][1:]):
                        sektory[max_sector-1].append(sektory[max_sector][0])
                        sektory[max_sector] = sektory[max_sector][1:]
                    else:
                        #print ("in middle right = left move to left to se nevyplati")
                        stop_it = 1
                    # reclaculate


        max_sector = get_max_sector(sektory, K)
        #print("max_sector", max_sector)
        #print("at the end -", sektory)

    return sum(sektory[get_max_sector(sektory, K)])

# small_random_ones
# random values {0, 1}, N = 100✘WRONG ANSWER
# got 4 expected 3
# 1.0.040 sOK
# 2.0.040 sOK
# 3.0.040 sOK
# 4.0.040 sWRONG ANSWER, got 4 expected 3
# ▶medium_zeros
# many zeros and 99 in the middle, length = 15,000✘TIMEOUT ERROR
# running time: 3.016 sec., time limit: 0.336 sec.
# 1.3.016 sTIMEOUT ERROR, running time: 3.016 sec., time limit: 0.336 sec.
# 2.0.056 sOK
# 3.0.060 sWRONG ANSWER, got 297 expected 99
# 4.0.064 sOK
# ▶medium_random
# random values {1, 100}, N = 20,000✘WRONG ANSWER
# got 203157 expected 202810
# 1.0.096 sOK
# 2.0.072 sWRONG ANSWER, got 203157 expected 202810
# 3.0.092 sWRONG ANSWER, got 101753 expected 101425
# 4.0.068 sWRONG ANSWER, got 1331 expected 1048
# ▶large_random
# random values {0, ..., MAX_INT}, N = 100,000✘WRONG ANSWER
# got 71618444 expected 71456005
# 1.0.516 sWRONG ANSWER, got 71618444 expected 71456005
# 2.0.240 sWRONG ANSWER, got 9098298 expected 8935266
# 3.0.240 sWRONG ANSWER, got 776724 expected 503942
# 4.8.000 sTIMEOUT ERROR, Killed. Hard limit reached: 8.000 sec.
# ▶large_random_ones
# random values {0, 1}, N = 100,000✘WRONG ANSWER
# got 469 expected 452
# 1.0.172 sOK
# 2.0.400 sOK
# 3.0.684 sWRONG ANSWER, got 469 expected 452
# 4.1.772 sTIMEOUT ERROR, running time: 1.772 sec., time limit: 1.264 sec.
# ▶all_the_same
# all the same values, N = 100,000✘WRONG ANSWER
# got 19000000 expected 18870000
# 1.0.140 sOK
# 2.0.140 sOK
# 3.0.180 sWRONG ANSWER, got 19000000 expected 18870000
# 4.0.244 sOK

#A = [2, 1, 5, 5, 1, 2, 2, 2]
A= [0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1]
A=[3, 4, 5, 6, 7, 8]
A=[1, 3, 1, 3, 2, 1, 3]
K = 3
M = 5
print( solution(K,M,A) )
