import sqlite3

def solution(x, y, d):
    if d <= 0:
        print("Takhel tam nedojdu")
        return 0
    if x * y <= 0 or y < x:
        print("spatny vstup")
        return 0
    steps = (y-x)//d
    #print(steps)
    if ((y-x)%d) > 0:
        steps += 1
    return steps

A = [1,2,3,4,5]
X = 10
Y = 85
D = 30
print(solution(X,Y,D))