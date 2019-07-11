def mystere(t):
    X = 0
    for i in range (0,len(t)):
        X = X + t[i]
    return  X/len(t)

t = [5, 9, 2, 7, 10, 1, 15]
print(mystere(t))
