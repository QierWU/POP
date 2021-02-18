'''
#			Le script permet de créer un fichier exploitable par cytoscape afin de relier des noms de gene à des Event ainsi que des Event à des AOP etc...
#
#			Il s'execute  de la manière suivante  ~Bureau/Rayane/Comptox/Cyto$ python3 Merge_table.py Tableau_Comptox_final.csv
#
#			Tableau_Comptox_final.csv est le fichier comprenant toutes les informations Comptox/Toxcast pour chaque composé ( Compound, Gene name , AOP , Event, etc..)
#
#
'''
import csv 
import sys
#
#
nomfichier = sys.argv[1]
#
#
with open(nomfichier, newline='') as csvfile1 :
	Tableau = csv.reader(csvfile1, delimiter = ';') 
	Gene_Name = []
	AOP = []
	AOP_name = []
	Event = []
	for row in Tableau :
		
		Gene_Name.append(row[2])
		AOP.append(row[3])
		AOP_name.append(row[4])
		Event.append(row[5])
		
del Gene_Name[0]
del Event[0]
del AOP[0]
del AOP_name[0]
#
#
#
#
dico={}
temp=[]
c=0
with open('Gene_MIE_AOP_Name_2.csv','w') as out :
	out.write("{};{};{};{};{}\n".format('Gene_Name', 'Event',  'AOP','AOP_Name', 'Occurence'))
	for i in range(len(Gene_Name)):
		ligne = Gene_Name[i]+Event[i]
		if ligne not in dico :
			dico[ligne] = 1			
			c=0
		else :
			dico[ligne]+=1
			
	for i in range(len(Gene_Name)):
		ligne = Gene_Name[i]+Event[i]
		
		if ligne not in temp :
			temp.append(ligne)
			if Event[i] != "-" and Gene_Name!= "-"	and Event[i] != "" : 
				out.write("{};{};{};{};{}\n".format(Gene_Name[i], Event[i],  AOP[i],AOP_name[i], dico[ligne]))

		
	

