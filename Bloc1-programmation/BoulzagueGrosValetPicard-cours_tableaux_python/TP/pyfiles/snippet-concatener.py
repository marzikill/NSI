def concatener(t1, t2):
    # Renvoie le tableau constitué des éléments de la
    # liste t1 puis des éléments de la liste t2.
    # Marche aussi avec des listes vides (merci Python)
    n1 = len(t1)
    n2 = len(t2)
    t = [0]*(n1 + n2)
    for i in range(n1):
        t[i] = t1[i]
    for j in range(n2):
        t[n1 + j] = t2[j]
    return t
