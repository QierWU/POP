#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
#				PREDICTION A PARTIR DU FICHIER MODELE COMPORTANT LES ASSOCIATIONS ENTRE PROTEINE POUR UN COMPOSE X
#
##					
#				
#					LE SCRIPT S'UTILISE COMME SUIT : $ python pred2.py 44BPF-87g-CompTox.txt outfile_Scoring.csv
#
#					44BPF-87g-CompTox.txt correspond au fichier contenant la liste de protéines où le composé X est impliqué, avec une protéine par ligne
#					'outfile_Scoring.csv' correspond au fichier modèle avec les Associaations Prot-Prot et les score BIN et PUL 
#
#
#				LES FICHIERS DE SORTIE SERONT GENERES DE LA MANIERE SUIVANTE :  ( les XXXX seront remplacés par le nom de fichier d'entrée )
#
#																				- Fichier avec les associations et scores = 'Con__XXXXXX.con'
#																				- Fichier avec les prtéines non trouvées dans le modèle ='Not_Found__XXXXXX.txt' 
#
#### Importation des outils utiles et nécessaires pour l'execution du script 
import sys
import csv
import os

file_L_prot_comp= sys.argv[1] #Création de la variable portant le nom de fichier de la liste de protéines du composé X
modele_file = sys.argv[2]	  #Création de la variable portant le nom du fichier modèle
#
#
#### Création des Listes de Protéines et de Scores à partir du fichier 'outfile_Scoring.csv'
try :
	with open(modele_file, newline='') as csvfile1 :
		Scoring_Table=csv.reader(csvfile1, delimiter = ';') 
		L_Prot1_Scoring = []
		L_Prot2_Scoring = []
		L_Score_Bin = []
		L_Score_Pul = []
		for row in Scoring_Table :
			L_Prot1_Scoring.append(row[0])
			L_Prot2_Scoring.append(row[1])
			L_Score_Bin.append(row[2])
			L_Score_Pul.append(row[3])
		del(L_Prot1_Scoring[0])
		del(L_Prot2_Scoring[0])
		del(L_Score_Bin[0])
		del(L_Score_Pul[0])
except IndexError :
	with open(modele_file, newline='') as csvfile1 :
		Scoring_Table=csv.reader(csvfile1, delimiter = '\t') 
		L_Prot1_Scoring = []
		L_Prot2_Scoring = []
		L_Score_Bin = []
		L_Score_Pul = []
		for row in Scoring_Table :
			L_Prot1_Scoring.append(row[0])
			L_Prot2_Scoring.append(row[1])
			L_Score_Bin.append(row[2])
			L_Score_Pul.append(row[3])
		del(L_Prot1_Scoring[0])
		del(L_Prot2_Scoring[0])
		del(L_Score_Bin[0])
		del(L_Score_Pul[0])
#
#
#
#### Création de la Liste de protéines du composé X
Liste_Prot_Comp_X = []
with open(file_L_prot_comp, "r") as File_X :
	
	for ligne in File_X :
		Liste_Prot_Comp_X.append(ligne.strip())
#		
#
#	
#### Création des deux fichiers avec les Assciations retrouvées pour le Composé X et les scores Associés
#### Ainsi que création d'un fichier texte avec les protéines non retrouvées dans le modèle
filevar_con = "Con__"+os.path.splitext(file_L_prot_comp)[0]+".con"
filevar_NF = "Not_Found__"+os.path.splitext(file_L_prot_comp)[0]+".txt"
Not_found = []
temp1=[]
temp2=[]
with open(filevar_con, 'w') as out1, open(filevar_NF, 'w') as out2 :
	out1.write("{};{};{};{}\n".format('Protein 1', 'Protein 2', 'Score Bin', 'Score Pul'))
	for i in range(len(L_Prot1_Scoring)):	
		
		for PX in Liste_Prot_Comp_X : 
			
			if ((PX in L_Prot1_Scoring) or (PX in L_Prot2_Scoring)) :
				
				if PX == L_Prot1_Scoring[i] or PX == L_Prot2_Scoring[i] :
					if L_Prot1_Scoring[i]+L_Prot2_Scoring[i] not in temp1 or L_Prot2_Scoring[i]+L_Prot1_Scoring[i] not in temp2 :
						temp1.append(L_Prot1_Scoring[i]+L_Prot2_Scoring[i])
						temp2.append(L_Prot2_Scoring[i]+L_Prot1_Scoring[i])
						# print(temp1)
						out1.write("{};{};{};{}\n".format(L_Prot1_Scoring[i], L_Prot2_Scoring[i], L_Score_Bin[i], L_Score_Pul[i]))

				
				
			else : 
				if PX not in Not_found :
					
					Not_found.append(PX)
					out2.write("{}\n".format(PX))				
