#
#
#
#			CE SCRIPT PERMET DE LISTER LES PROTEINES QUI INTERAGISSENT AVEC
#			UN COMPOSE SUR LA BASE D'UN FICHIER CSV COMPORTANT LES INFORMATIONS DEPUIS
#			BASES DE DONNEES COMPTOX/TOXCAST , SELON LA STRUCTURE SUIVANTE :
#
#			ESSAI,  GENE NAME, AOP, EVENT, AC50, logAC50, INTENDED TARGET FAMILY (=>> GENE NAME//PROTEIN EN DEUXIEME COLONNE)
#
#
#			LE SCRIPT CREE UN DOSSIER POUR CHAQUE COMPOSE AVEC DANS LE DOSSIER LE FICHIER 
#			COMPRENANT LA LISTE DES PROTEINES ( EN FORMAT .TXT)
#
#
#					LE FICHIER OUTFILE_SCORING DOIT ETRE DANS LE MEME DOSSIER QUE LE SCRIPT OU ETRE INDIQUE EN ARGUMENT : 
#
#
#			=>> EXECUTION DU SCRIPT : $ python List_prot_script2.py  (avec fichier outfile_Scoring dans le dossier ) 
#							OU BIEN   $ python List_prot_script2.py outfile_Scoring.csv
#
#			NB : Doit être exécuté dans le dossier contenant tous les fichiers csv contenant l'info COMPTOX/TOXCAST pour chacun des composés
#				 !! Le script va créer des dossiers pour chaque fichier csv présent dans le dossier courant. !!
#
#
#			SELON LES DELIMITEURS CHOISIS POUR ENREGISTRER LES INFOS DE CHAQUE COMPOSE DANS DES FICHIERS CSV SEPARES , IL FAUDRA ADAPTER LE SCRIPT (COMMANDE with open(compfile, nexline=''))
#
#					
#
#
#
import csv
import os 
import sys
import codecs
#
#
ALL_files = os.listdir('./')
#
#
#
#
try : 
	modele_file=sys.argv[1]
except IndexError :
	modele_file = 'outfile_Scoring.csv'
	
for comp_file in ALL_files :
	
	dirName = os.path.splitext(comp_file)[0]
		
	
	
	if comp_file[-3:] == 'csv' :
		if not os.path.exists(dirName):
			os.mkdir(dirName)
			print("Directory " , dirName ,  " Created ")
		else:    
			print("Directory " , dirName ,  " already exists ")
			
			
		with open(comp_file, newline='') as csvfile :
			Lprot=[]
			Tableau = csv.reader(csvfile, delimiter = '\t')
			
			try  : 

				for row in Tableau :
					colprot=row[1].strip().upper()
					if colprot not in Lprot and colprot != '-' :
						Lprot.append(colprot)
					
			except csv.Error :
				f = codecs.open(comp_file, "r+b", "utf_16")
				Tableau = csv.reader(f, delimiter = '\t')
				# Tableau.next()
				for row in Tableau :
					colprot=row[1].strip().upper()
					if colprot not in Lprot and colprot != '-' :
						Lprot.append(colprot)
					
			del Lprot[0]
			outname = dirName+'/Liste_prot_'+comp_file[0:-3]+'txt'
			with open(outname, 'w') as outfile :
				for prot in Lprot :
					outfile.write('{}\n'.format(prot))
			print("{}{:45}{}".format('file :  ', outname, "  Done\n"))
			
			
			
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
			with open(outname, "r") as File_X :
				
				for ligne in File_X :
					Liste_Prot_Comp_X.append(ligne.strip())
			#		
			#
			#	
			#### Création des deux fichiers avec les Assciations retrouvées pour le Composé X et les scores Associés
			#### Ainsi que création d'un fichier texte avec les protéines non retrouvées dans le modèle
			filevar_con = dirName+"/Con__"+os.path.splitext(comp_file)[0]+".con"
			filevar_NF = dirName+"/Not_Found__"+os.path.splitext(comp_file)[0]+".txt"
			Not_found = []
			temp1=[]
			temp2=[]
			with open(filevar_con, 'w') as out1, open(filevar_NF, 'w') as out2 :
				out1.write("{};{};{};{}\n".format("Prot 1", "Prot 2", "Score Bin", "Score Pul"))

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
						
			#
