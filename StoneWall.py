#když je hodnota větší než předešlé přidáváme kameny
#když je následující hodnota nižší odebíráme kameny dokud výška větší než hodnota,
#    když nám tam nezůstane kámen přidáme nový správné výšky

def solution(A):
    bricks=[]
    bricks_cout=0
    for a in A:
        if sum(bricks) == a:
            pass
        elif sum(bricks) < a:
            bricks += [a - sum(bricks)]
            bricks_cout+=1
        else:# sum(bricks) > a
            while sum(bricks) > a:
                del bricks[-1]
            if sum(bricks) < a:
                bricks += [a - sum(bricks)]
                bricks_cout+=1
    return bricks_cout

A=[8,8,5,7,9,8,7,4,8]
print(solution(A))