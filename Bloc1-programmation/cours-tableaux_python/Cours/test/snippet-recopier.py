from math import *

def recopie2(t):
    n = len(t)
    tc = []*n
    for i in range(n):
        tc[i] = t[i]
    return tc

t2 = [4, 5, 8, 7]
print('Tableau à recopier', t2)
tc2 = recopie2(t2)
#print(recopie(t))
