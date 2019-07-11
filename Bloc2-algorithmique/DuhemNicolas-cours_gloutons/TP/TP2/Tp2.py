liste= [ [1, 5, 6], [8, 10, 2], [3, 3, 5],[4, 8, 1] ]

def extraire(t,n):
	for i in range(1,len(t)):
		v = t[i][n]
		j = i-1
		while(j>=0 and t[j][n]>v):
			t[j+1],t[j] = t[j],t[j+1]
			j = j-1
		t[j+1][n] = v
	return t

print(extraire(liste,1))
print(extraire(liste,2))

def gloutonP(l,maxi):
	tmp=[x for x in l]
	tmp.sort(key=lambda tup: tup[1],reverse=True)
	valeur=0
	poids=0
	i=0
	solution=[]   
	while i<len(tmp):
		if (poids+tmp[i][1]) <=maxi:
			solution.append(tmp[i])
			poids +=tmp[i][1]
			valeur+=tmp[i][0]
		i+=1
	reponse=[1 if x in solution else 0 for x in l]        
	
	return reponse,valeur,poids


print(gloutonP(liste,30))

def gloutonV(l,maxi=30):
	tmp=[x for x in l]
	l.sort(key=lambda tup: tup[0],reverse=True)
	valeur=0
	poids=0
	i=0
	solution=[]
	while i<len(tmp):
		if (poids+tmp[i][1]) <=maxi:
			solution.append(tmp[i])
			poids +=tmp[i][1]
			valeur+=tmp[i][0]
		i+=1
	reponse=[1 if x in solution else 0 for x in tmp]
		
	return reponse,valeur,poids
print(gloutonV(liste,30))


def gloutonVPP(l,maxi=30):
	tmp=[x for x in l]
	l.sort(key=lambda tup: tup[0]/tup[1],reverse=True)
	valeur=0
	poids=0
	solution=[]
	i=0
	while i<len(tmp):
		if (poids+tmp[i][1]) <=maxi:
			solution.append(tmp[i])
			poids +=tmp[i][1]
			valeur+=tmp[i][0]
		i+=1
	reponse=[1 if x in solution else 0 for x in tmp]
	
	return reponse,valeur,poids

print(gloutonVPP(liste,30))



    
