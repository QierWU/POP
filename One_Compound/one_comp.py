'''	
#				EXECUTION DU SCRIPT : $ python3 one_comp.py Con__anthracene.con Gene_MIE_AOP_Name_2.csv
#
#						Con__44BPF-87g-CompTox.con = fichier de prédiction généré par le script pred2.py
#						Gene_MIE_AOP_Name_2.csv		   = fichier regroupant dans un tableau les protéines, les Event et les AOP du modèle
#
#
#					Le fichier de sortie généré contient les proteines et les Event, AOP associés pour un composé donné
#
'''
import sys
import csv
import os
import codecs
comp_file = sys.argv[1]
merge_name = sys.argv[2]
comp_name=comp_file[:-4]
if comp_file[-3:]=='con' :
########	Lecture de la table si le fichier de départ est Con__
	with open(comp_file, newline='') as csvfile1 :
			Con_Table=csv.reader(csvfile1, delimiter = '\t') 
			L_Prot = []
			for row in Con_Table :
				if row[0] not in L_Prot :
					L_Prot.append(row[0])
				if row[1] not in L_Prot :
					L_Prot.append(row[1])
			del(L_Prot[0])
			del(L_Prot[0])

########	Lecture de la table si le fichier de départ est un tableau de Comptox  avec les proteines en 2ème colonne (Gene Name) 
		
if comp_file[-3:]=='csv' :
	with open(comp_file, newline='') as csvfile :
				L_Prot=[]
				Tableau = csv.reader(csvfile, delimiter = '\t')
				
				try  : 

					for row in Tableau :
						colprot=row[1].strip().upper()
						if colprot not in L_Prot and colprot != '-' :
							L_Prot.append(colprot)
						
				except csv.Error :
					f = codecs.open(comp_file, "r+b", "utf_16")
					Tableau = csv.reader(f, delimiter = '\t')
					# Tableau.next()
					for row in Tableau :
						colprot=row[1].strip().upper()
						if colprot not in L_Prot and colprot != '-' :
							L_Prot.append(colprot)
						
				del L_Prot[0]		
###########	
with open(merge_name, newline='') as csvfile1 :
		Scoring_Table=csv.reader(csvfile1, delimiter = ';') 
		L_Gene_name = []
		L_Event = []
		L_AOP = []
		L_AOP_name = []
		for row in Scoring_Table :
			L_Gene_name.append(row[0])
			L_Event.append(row[1])
			L_AOP.append(row[2])
			L_AOP_name.append(row[3])
		del(L_Gene_name[0])
		del(L_Event[0])
		del(L_AOP[0])
		del(L_AOP_name[0])
#### Variable nom de fichier outfile
outname=comp_name+'_Event_AOP_name.csv'

#### Création du fichier outfile 
with open(outname, 'w') as outfile :
	outfile.write('{};{};{};{};{}\n'.format('Compound','Protein','Event','AOP','AOP_name'))
	for i in range(len(L_Gene_name)) : 
		for prot in L_Prot : 
			if L_Gene_name[i] == prot :
					outfile.write('{};{};{};{};{}\n'.format(comp_name[5:],L_Gene_name[i], L_Event[i], L_AOP[i], L_AOP_name[i]))
		
