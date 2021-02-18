#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
#           L'EXECUTION DU SCRIPT SE FAIT À L'EMPLACEMENT DU FICHIER CONTENANT LES INFORMATIONS DES COLONNES PROT 1 , 2 ET OVERLAPS SOUS FORME DE TABLEAU (Prot-POP-unix.con) 
#
#							CE FICHIER DOIT ETRE PASSE EN ARGUMENT DE LA MANIERE SUIVANTE : $ python3 script.py Prot-POP-unix.con
#
'''
# Importation des fonctions et bibliothèques nécessaires à l'éxecution du script  
import csv
import sys
from math import log10
#
#
#### Fonction qui Calcule et renvoi le Score BIN entre deux protéines
def score_bin(prot1, prot2) :
	LPA = []
	LPB = []
	Ldouble=[]
	for i in range(len(List_Prot_1)) :
		if List_Prot_1[i] == prot1 :
			LPA.append(List_Prot_2[i])
			
		if List_Prot_2[i] == prot1 :
			LPA.append(List_Prot_1[i])
		
		if List_Prot_1[i] == prot2 :
			LPB.append(List_Prot_2[i])
			
		if List_Prot_2[i] == prot2 :
			LPB.append(List_Prot_1[i])
	
	for prot in LPA :
		if prot in LPB:
			Ldouble.append(prot)
			
	for doubl in Ldouble :
		if doubl in LPA :
			LPA.remove(doubl)
		if doubl in LPB :
			LPB.remove(doubl)
	
			
	NA= len(LPA)
	NB= len(LPB)
	S = -log10((NA+1)*(NB+1))
	return S
#
#
#### Fonction qui Calcule et renvoi le Score PUL entre deux protéines
def score_pul(prot1, prot2, OS):
	NA = 0
	NB = 0
	NA_int_B =	int(OS)
	
	for proteine in List_Prot_1 :
		if prot1 == proteine :
			NA+=1
		if prot2 == proteine :
			NB+=1
			
	for proteine in List_Prot_2 :
		if prot1 == proteine :
			NA+=1
		if prot2 == proteine :
			NB+=1
			

	NAUB = NA + NB - NA_int_B
	S2 = log10((NA_int_B * NAUB )/((NA+1)*(NB+1)))
	return S2
#
#
# Récupère sous forme de liste les éléments du tableau donné en argument lors de l'execution du script en éliminant les noms de colonnes 
File_table = sys.argv[1]
with open(File_table, newline='') as csvfile :
	GenTable=csv.reader(csvfile, delimiter = '\t') 
	List_Prot_1 = []
	List_Prot_2 = []
	Nb_Comp_asso = []
	for row in GenTable :
		List_Prot_1.append(row[1])
		List_Prot_2.append(row[2])
		Nb_Comp_asso.append(row[3])
del(List_Prot_1[0])
del(List_Prot_2[0])
del(Nb_Comp_asso[0])
#
#
#### Fonction MAIN ####
def main():

#### Création du fichier contenant les colonnes "Prot 1","Prot 2","score BIN", "score PUL"  : outfile_Scoring.csv
			
	with open('outfile_Scoring.csv', 'w') as outfilescoring :
		outfilescoring.write("{};{};{};{}\n".format("Prot 1","Prot 2","score BIN", "score PUL"))
		for i in range(len(List_Prot_1)) : 
			score_BIN = score_bin(List_Prot_1[i],List_Prot_2[i])
			score_PUL = score_pul(List_Prot_1[i],List_Prot_2[i],Nb_Comp_asso[i])
			outfilescoring.write("{};{};{};{}\n".format(List_Prot_1[i],List_Prot_2[i],score_BIN, score_PUL))

#### Execution du MAIN ####
main()
