# coding: utf-8

import csv
import matplotlib.pyplot as plt

coord=[]
cr = csv.reader(open("iris.csv","rb"))
for row in cr:
	coord.append([row[0],row[1],row[2]])

coord.pop(0)

for i in range(len(coord)):
	if((coord[i][2])=='0'):
		plt.scatter(coord[i][0], coord[i][1], color='g', label='setosa')
	elif(coord[i][2]=='1'):
		plt.scatter(coord[i][0], coord[i][1], color='r', label='virginica')
	elif(coord[i][2]=='2'):
		plt.scatter(coord[i][0], coord[i][1], color='b', label='versicolor')
#plt.legend()
plt.axis([0, 6, 0, 3])

#plt.scatter(5.1, 1.7, color='black')


plt.show()
# affiche la figure à l'écran.



