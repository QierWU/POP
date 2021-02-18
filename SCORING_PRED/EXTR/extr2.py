#
#
#
#                EXECUTION DU SCRIPT DE LA MANIERE SUIVANTE =>>>     $ python extr2.py Prot-POP-unix.che Prot-POP-unix_2.con
#					C'est à dire : python script.py composés.che connexions_avc_scores.con
#
#				LE FICHIER AVEC LA LISTE DES COMPOSES : 'Liste_CAS_CID_Smiles_Class.csv' DOIT ETRE DANS LE MEME DOSSIER QUE CE SCRIPT
#
#### Importation des outils utiles et nécessaires pour l'execution du script 
import sys
import csv
import os
#
#### Création de la liste de tous les composés étudiés à partir du fichier 'Liste_CAS_CID_Smiles_Class.csv'
with open('Liste_CAS_CID_Smiles_Class.csv', newline='', encoding ='ISO-8859-1') as csvfile1 :
	GenTable=csv.reader(csvfile1, delimiter = ',') 
	ALL_COMP = []
	for row in GenTable :
		compname=(row[2].strip())
		if " " in compname : 
			compname=compname.replace(" ", "")			
		ALL_COMP.append(compname)
	del(ALL_COMP[0])
#
#
#### Création de la liste correspondant au fichier 'Prot-POP-unix.che'
File_chem = sys.argv[1]
with open(File_chem, newline='') as csvfile2 :
	GenTable=csv.reader(csvfile2, delimiter = '\t') 
	List_Comp = []

	for row in GenTable :
		List_Comp.append(row[1])
	del(List_Comp[0])
#
#
#### Création des listes contenant les noms de prot et les scores à partir du fichier 'Prot-POP-unix.con'
File_conn = sys.argv[2]
with open(File_conn, newline='') as csvfile3 :
	GenTable=csv.reader(csvfile3, delimiter = '\t') 
	List_Prot_1 = []
	List_Prot_2 = []
	Score_Bin = []
	Score_PUL = []
	for row in GenTable :
		List_Prot_1.append(row[1])
		List_Prot_2.append(row[2])
		Score_Bin.append(row[7])
		Score_PUL.append(row[8])
	del(List_Prot_1[0])
	del(List_Prot_2[0])
	del(Score_Bin[0])
	del(Score_PUL[0])
#
#
#
#### Création de l'ensemble des fichiers ( 1 / composé), et informant dans quelle(s) association(s) Prot-Prot il intervient et quelles sont les scores associés, regroupé dans un dossier "Results"
outdir="Results/"
os.mkdir(outdir)
for comp in ALL_COMP :

	L_ID = []			#Initialisation de la Liste qui contiendra les ID d'intérêt
	
	#### Compte et liste les ID où figure le composé X .

	for i in range(len(List_Comp)):
		if comp in List_Comp[i] :
			L_ID.append(i)
			
	if len(L_ID) == 0 : #Condition qui permet de renommer et créer spécialement les composés qui ne sont impliqués dans aucune association et qui n'auront donc pas d'informations dans leur fichier de sortie
		filevar="0_EMPTY_RES_"+comp+".csv"
		outname = outdir+filevar
		with open(outname,'w') as outfile :	
			outfile.write("{}\t{}\t{}\t{}\t{}\n".format("ID", "Proteine 1", "Proteine 2", "Score Bin", "Score PUL"))	
			for idnum in L_ID :
				outfile.write("{}\t{}\t{}\t{}\n".format("No_Results", "No_Results", "No_Results","No_Results","No_Results"))
				
	elif  ":" in comp :  # Condtion qui permet de renommer  et créer les noms de fichiers lorsque le nom de composé contient des ":" ou des ","
			comp = comp.replace(":", "")
			filevar=comp+".csv"
			outname = outdir+filevar
			with open(outname,'w') as outfile :
				outfile.write("{}\t{}\t{}\t{}\t{}\n".format("ID", "Proteine 1", "Proteine 2", "Score Bin", "Score PUL"))	
				for idnum in L_ID :
					outfile.write("{}\t{}\t{}\t{}\t{}\n".format(idnum, List_Prot_1[idnum], List_Prot_2[idnum], Score_Bin[idnum], Score_PUL[idnum]))
					
	else : # Création du reste des fichiers qui ne font pas partie des exceptions
		filevar=comp+".csv"
		outname = outdir+filevar			
		with open(outname,'w') as outfile :	
			outfile.write("{}\t{}\t{}\t{}\t{}\n".format("ID", "Proteine 1", "Proteine 2", "Score Bin", "Score PUL"))	
			for idnum in L_ID :
				outfile.write("{}\t{}\t{}\t{}\t{}\n".format(idnum, List_Prot_1[idnum], List_Prot_2[idnum], Score_Bin[idnum], Score_PUL[idnum]))	
#
#
#
#
######
