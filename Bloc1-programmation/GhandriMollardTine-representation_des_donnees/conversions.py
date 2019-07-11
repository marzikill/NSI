# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 13:25:26 2019

@author: noel.tine
"""

#exercice3
#convertir un nombre decimal en binaire 
def decimalBinaire(n):
    """Convertit un nombre en binaire"""
    q = -1
    res = ''
    while q != 0:
        q = n//2
        r = n%2
        res = str(r) + res
        n = q
    return res

#print(decimalBinaire(121))
#print(decimalBinaire(255))
#print(decimalBinaire(2))


#exercice4
#convertir un nombre decimal en hexadécimal 
def decimalHexa(n):
    e=''
    while n!=0:
        r=n%16
        if r==10:
            e='A'+e
        if r==11:
            e='B'+e
        if r==12:
            e='C'+e
        if r==13:
            e='D'+e
        if r==14:
            e='E'+e
        if r==15:
            e='F'+e
        if r<10:
            e=str(r)+e
        n=n//16
        if (e==''):
            e='0'
    return(""+e)
        
   
#print(decimalHexa(11))
#a=46
#print(decimalHexa(a))
#print(hex(a))
#if(hex(a)!=decimalHexa(a)):
#    print("erreur")
#else:
#    print("ok")


#exercice7
#convertir un nombre binaire en decimal 

def binaireDecimal(x): 
    nb = 0 
    j = len(x)-1 #puissance 
    for i in x: 
        nb = nb + int(i)*2**j 
        j = j-1
    return nb

#print(binaireDecimal(1000'))
#print(binaireDecimal('11110'))
#print(binaireDecimal('1000111'))


#exercice8
#convertir un nombre hexadecimal en decimal 
listehexa=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
listebinaire=["0000","0001","0010","0011","0100","0101","0110","0111","1000",
              "1001","1010","1011","1100","1101","1110","1111"]

def binaireDecimal(string):
    x=len(string)-1
    n=0
    res=0
    while x!=-1:
        if string[x]=="1":
            res=res+2**n
        n=n+1
        x=x-1
    return res

def hexaBinaire(string):
    res=""
    for x in range(len(string)):
        i=listehexa.index(string[x])
        res=res+listebinaire[i]
    return res

def hexaDecimal(string):
    return binaireDecimal(hexaBinaire(string))


print(hexaDecimal("A"))
print(hexaDecimal("F"))
print(hexaDecimal("16"))
print(hexaDecimal("FF"))



#exercie14
#addition binaire: Manuel ISN G. Dowek

#n = [0, 0, 0, 0, 0, 0, 1, 1]
#p = [0, 0, 0, 0, 0, 0, 1, 0]

def addition_binaire(x,y):
    r = []
    c = False
    for i in range(7, -1, -1):
        a = x[i]
        b = y[i]
        unite = (a and not(b) and not(c)) or\
            (not(a) and b and not(c)) or\
            (not(a) and not(b) and c) or\
            (a and b and c)
        r = [int(unite)] + r
        c = (a and b) or (b and c) or (a and c)
        
    r = [int(c)] + r

    return r

#print(addition_bin(n,p))
print(addition_binaire([0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,1]))  
print(addition_binaire([0,0,0,0,0,0,1,0],[0,0,0,0,0,0,1,0]))
print(addition_binaire([0,0,0,0,0,0,1,0],[0,0,0,0,0,0,1,1]))
print(addition_binaire([0,0,0,0,1,1,0,0],[0,0,0,1,0,0,0,0]))
