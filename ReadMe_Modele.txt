Une fois l'ACP réalisée et la table Comptox_ALL_compounds_matrix obtenue, la seconde partie du projet est de réaliser un modèle de prédiction ainsi qu'un Prot Prot Association Network (PPAN) à partir des données, notamment à partir de la table évoquée précédemment.
Ainsi à partir de différents scripts, différents fichiers ont été générés. 
Un premier Script executé par Mme Audouze, permet l'obtention des fichiers Prot-POP-unix.che et Prot-POP-unix.con . Ce script n'est donc pas présent dans mes dossiers.
Prot-POP-unix.con regroupe par ligne des scores calculés pour chaque association protéine protéine, les protéines qui y sont impliquées et un identifiant numérique.
Prot-POP-unix.che regroupe les chemicals qui forment l'association protéine protéine ( identifiable par son ID ).

Les scripts suivants ont été réalisés afin d'être executables sous python 3.7.3, et d'une manière plus générale sous python 3.

À partir de deux formules de scoring disponibles dans le fichier 'W02_scoring_of_PPI .pdf' et des données, la première étape a été de prédire les scores pour chaque association prot-prot. 
	script_scoring.py : 
		Il permet de générer un nouveau fichier avec les deux protéines assoociées et les deux scores calculés ( 4 colonnes en tout) 
		Il s'éxecute de la manière suivante => $ python script.py Prot-POP-unix.con
		Il génère un fichier de sortie ' outfile_Scoring.csv ' 

Ensuite des scripts de prédiction à partir du fichier outfile_Scoring ont été réalisés. Il y a 2 scripts : 
	extr2.py :
		Ce premier script sert à tester les molécules du modèle.
		Il s'éxecute de la manière suivante => $ python extr.py Prot-POP-unix.che Prot-POP-unix_2.con
		Prot-POP-unix_2.con correspond au fichier Prot-POP-unix.con auquel on a ajouté les deux colonnes de scores du fichier outfile_Scoring
		Le fichier avec a liste des composés : 'Liste_CAS_CID_Smiles_Class.csv' doit être dans le même dossier que ce script.
	pred2.py
		Ce second script permet de tester des molécules qui sont extérieurs à la liste de composés et donc extérieurs au modèle.
		Il s'éxecute de la manière suivante => $ python pred2.py 44BPF-87g-CompTox.txt outfile_Scoring.csv
		44BPF-87g-CompTox.txt correspond au fichier contenant la liste de protéines où le composé X est impliqué, avec une protéine par ligne
		'outfile_Scoring.csv' correspond au fichier modèle avec les Associations Prot-Prot et les score BIN et PUL
		Cela génère deux fichiers de sorties :
			Fichier avec les associations et scores => 'Con__XXXXXX.con'
			Fichier avec les protéines non trouvées dans le modèle => 'Not_Found__XXXXXX.txt' 
		Ainsi l'éxecution de ce script nécessite d'avoir la liste de protéines qui intéragissent avec un composé.
		
Si on a un ensemble de composés à tester et que l'on a pas leur liste de protéines avec lesquels ils intéragissent, il existe le script suivant : 
	List_prot_script2.py :
		Pour utiliser ce script, il est primordial de compiler les infos Comptox/Toxcast pour chaque composé dans des fichiers csv séparés avec comme nom => nom_composé.csv
		Une fois cette tâche effectuée, il suffit de se placer dans le dossier avec tous les fichiers que l'on vient de créer, dy ajouter le fichier :
			'outfile_Scoring.csv'
		Puis d'éxecuter le script d'une des manières suivantes : 
			$ python List_prot_script2.py  (avec fichier outfile_Scoring dans le dossier )
			$ python List_prot_script2.py outfile_Scoring.csv
		Ce script va créer un dossier séparé pour chaque composé ( pour chaque fichier .csv) et va dans chaque dossier créer trois fichiers :
			Con__XXXX.con contenant les associations retrouvées et les scores BIN et PUL associés
			Liste_prot_XXXX.txt La liste des protéines qui intéragit avec le composé (selon CompTox/Toxcast)
			Not_Found_XXXX.txt La liste des protéines non retrouvées dans le modèle de départ
			
Enfin la dernière partie du projet est de visualiser les données sous forme de réseaux biologiques à l'aide du logiciel Cytoscape(version 3.7.1)
		