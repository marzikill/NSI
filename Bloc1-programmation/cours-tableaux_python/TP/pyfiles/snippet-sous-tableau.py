def sous_tableau(t, i, j):
    # Extrait le sous tableau constitué des éléments
    # d'indice compris entre i et j (exclu) du tableau
    # 0 < i < j <= len(t) : sinon IndexError
    n = j - i
    tprime = [0]*n
    for k in range(n):
        tprime[k] = t[k + i]
    return tprime
