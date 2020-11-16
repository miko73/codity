import sqlite3
diakritika = ['ě','š','č','ř','ž','ý','á','í','é','ď','ť','ň']
def solution(A, B):
   s = {x for x in A if x > 0}
   print(s)
   s2 = set(range(1, len(pismena)))
   print(s2)
   print(B)
   B.sort()
   print(B)
   for a in diakritika:
      print("[{0},{1},{2}]".format(a,str(a).upper(), str(str(a).upper()).lower()))

pismena=['a','s','d','f','g','s','d','f','h','w','e','r','u','p','q','ě','č','č','ě','č','í','á','ý','š','č','é']
cisla = [56,34,77,878,989,-232,545,656]
solution(cisla, pismena)