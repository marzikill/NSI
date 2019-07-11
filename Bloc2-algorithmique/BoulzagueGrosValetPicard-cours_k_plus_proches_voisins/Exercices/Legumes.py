def tri_Leg(L,x):
    Indice=0
    S=0
    inter=[]
    for i in range(len(L)):
        j=0
        nb0=0
        nb1=1
        while j < len(L[i]):
            if L[i][j] == x[j] and x[j] == 0:
                nb0 = nb0 + 1
            elif L[i][j] == x[j] and x[j] == 1:
                nb1 = nb1 + 1
            j=j+1    
        S = nb1/(7-nb0)
        inter.append([])
        inter[i].append(i)
        inter[i].append(S)
    for i in range(len(inter)):
        if i < (len(inter)-1):
            if inter[i][1] < inter[i+1][1]:
                S = i
            
    return "c'est un: ", L[S]   
legume=[["banane",0,0,1,0,1,1,0],["concombre",0,1,0,0,1,0,1],["litchi",0,1,0,1,0,0,1],["salade",0,1,0,1,0,0,1],["tomate",1,0,0,1,0,1,0]]
salade=["salade",0,1,0,1,0,0,1]
print(tri_Leg(legume,salade))
