def recopier(t):
    # Recopie le tableau t dans une nouvelle variable.
    n = len(t)
    copie = [0]*n
    for i in range(n):
        copie[i] = t[i]
    return copie
