def et_boule_de_gomme(t):
    X = t[0]
    for i in range (0,len(t)):
        if t[i] > X:
            X = t[i]
    return X

t = [5, 9, 3, 6, 10, 1, 15]
print(et_boule_de_gomme(t))
