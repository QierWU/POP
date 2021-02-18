'''
Ce script s'exécute directement de la manière suivante ~Bureau/Rayane/Comptox$ python3 Script_clean.py
Il génère le fichier Tableau_Comptox_final.csv
'''
import csv 
with open('Comptox_ALL_compounds_matrix_2.csv', newline='') as csvfile1 :
	Tableau = csv.reader(csvfile1, delimiter = ';') 
	Compound = []
	Name = []
	Gene_Name = []
	AOP = []
	AOP_Name = []
	Event = []
	Event_Name = []
	Event_Class = []
	AC50 = []
	logAC50 = []
	IntendedT_arget_Family = []
	
	for row1 in Tableau :

		Compound.append(row1[0].strip())
		Name.append(row1[1])
		Gene_Name.append((row1[2].strip()).upper())
		AOP.append(row1[3].strip())
		AOP_Name.append(row1[4].strip())
		Event.append(row1[5].strip())
		Event_Name.append(row1[6].strip())
		Event_Class.append(row1[7].strip())
		AC50.append(row1[8].strip())
		logAC50.append(row1[9].strip())
		IntendedT_arget_Family.append(row1[10].strip())

with open('Tableau_Comptox_final.csv','w') as out :
	for i in range(len(Name)):
		out.write("{};{};{};{};{};{};{};{};{};{};{}\n".format(Compound[i], Name[i], Gene_Name[i], AOP[i], AOP_Name[i], Event[i], Event_Name[i],  Event_Class[i], AC50[i], logAC50[i], IntendedT_arget_Family[i]))
