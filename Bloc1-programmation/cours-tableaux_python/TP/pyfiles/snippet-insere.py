def insere(t, i, e):
    # Insère l'élément e à l'indice i dans le tableau t.
    # i <= len(t) : sinon IndexError.
    # i = 0 : e inséré en début de tableau
    # i = len(t) : e inséré en fin de tableau
    n = len(t)
    tprime = [0]*(n+1)
    for k in range(i):
        tprime[k] = t[k]
    tprime[i] = e
    for k in range(i+1, n+1):
        tprime[k] = t[k-1]
    return tprime
