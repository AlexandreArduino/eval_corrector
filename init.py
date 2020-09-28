'''
BAALBAKY Alexandre 1ere C++
'''

try:
    import os
except:
    print("Désolé, il semble que le module os ne soit pas présent sur votre machine :(")
    input("Appuyez pour quitter ...")
    exit()

class EVAL(object):
    def __init__(self):
        self.init_project()
    def init_project(self):
        self.name = input("Veuillez entrer le nom de l'évaluation >>> ")
        try:
            os.mkdir(self.name)
        except:
            print("Ce nom est déjà utilisé")
            input("Appuyez pour recommencer ...")
            self.init_project()
        try:
            self.nb_ex = int(input("Nombre d'exercices >>> "))
        except:
            print("Ce n'est un nombre entier !")
            input("Appuyez pour recommencer ...")
            self.init_project()
        try:
            os.chdir(self.name)
        except:
            print("Erreur, le dossier " + self.name + " a été supprimé :(")
            input("Erreur 0x1\nAppuyez pour quitter ...")
            exit()
        try:
            os.mkdir("config")
        except:
            pass
        try:
            os.chdir("config")
        except:
            print("Erreur, le dossier config a été supprimé :(")
            input("Erreur 0x2\nAppuyez pour quitter ...")
            exit()
        conf = open('conf.snp', 'w')
        #Première écriture, pas besoin de \n
        conf.write(str(self.nb_ex))
        conf.close()
        os.chdir("../")
        for ex in range(self.nb_ex):
            try:
                os.mkdir("ex" + str(ex))
            except:
                pass
        #Création du dossier barème
        '''try:
            os.mkdir("barème")
        except:
            pass'''
        self.nb_q = []
        for q in range(self.nb_ex):
            try:
                self.nb_q.append(int(input("Nombre de questions de l'exercice " + str(q) + " >>> ")))
            except:
                print("Ce n'est pas une valeur entière !")
                input("Appuyez pour quitter, vous devez donc tout recommencer :( ...")
                exit()
            os.chdir("ex" + str(q))
            for questions in range(self.nb_q[q]):
                try:
                    os.mkdir("q" + str(questions))
                except:
                    pass
            os.chdir("../")
        os.chdir("config")
        file = open("confi.snp", "w")
        #On note le nombre de questions par ex
        for questions in range(len(self.nb_q)):
            file.write(str(self.nb_q[questions]) + "\n")
        file.close()
        os.chdir("../")
        os.chdir("../")
        if int(input("Souhaitez-vous lire le manuel ? 0/1 (les autres réponses valent 0 :)) >>> ")):
            self.readme()
        else:
            pass
        #en dehors des questions
        '''
        ex1 => 1q
        q :
        1 phrase d'intro => avec des mots clés
        calcul => la formule, les valeurs, et le résultat
        la phrase outro => mots clés
        '''
    def readme(self):
        try:
            os.system('cls')
        except:
            pass
        try:
            os.system('clear')
        except:
            pass
        print("Bienvenue dans le manuel d'utilisation d'eval_corrector !\n")
        print("Vous venez de créer une nouvelle évaluation => " + self.name + "\n")
        #On suppose que le répertoire est à /
        print("-"*50)
        os.chdir(self.name + "/config")
        file = open("conf.snp", "r")
        print("L'évalution est composée de " + str(file.read()) + " exercices.\n")
        file.close()
        file = open("confi.snp", "r")
        line = file.readline()
        q = 0
        while line:
            cache = list(line)
            for i in range(len(cache)):
                if cache[i] == '\n':
                    del cache[i]
            print("L'exercice " + str(q) + " comporte " + "".join(cache) + " questions.\n")
            line = file.readline()
            q += 1
        file.close()
        print("\n")
        print("Dans le répertoire de eval_corrector, il y a un dossier nommé " + self.name + ", il contient les ressources pour permettre au programme d'effectuer la correction :) .")
        print("Mais il faut entrer d'autres valeurs (ou critères) pour pouvoir le faire fonctionner (le programme).")
        print("Veuillez entrer dans ce dossier")
        input("Appuyez quand c'est fait ...")
        print("Explication de l'architecture du répertoire : \n\n\n" + "-"*50)
        print("- config : ")
        print("\tContient les fichiers de configuration générés par le programme, vous n'avez pas besoin d'y toucher.")
        print("\n\n- exN (remplacer N par un numéro) : ")
        print("\tCe sont les répertoires des exercices. Chaque exercice étant différent, il nécessite des données différentes.")
        print("Nous allons commencer par configurer le premier exercice, ensuite ce sera la même chose pour les autres :).")
        print("Entrez donc dans un des répertoires des exercices.")
        input("Appuyez quand c'est faut ...")
        print("\n")
        print("Effectivement, il y a encore des sous-dossiers :(), un pour chaque question :)")
        print("Il faut donc décomposer chaques questions, : ")
        print("\tcombien de points vaut-elle au total ?")
        print("\tquels éléments sont nécessaire en introduction (éléments obligatoires), combien de points valent-ils chacun ")
        print("\tquels éléments sont obligatoires dans le développement du calcul (formule, valeurs, résultats, unités), et leurs points")
        print("\tpareil pour la conclusion")
        print("\n")
        print("-"*50)
        print("On va commencer par l'introduction de la première question du premier exerice : ")
        #si pas de lecture du readme, générer tous les fichiers avant
        os.chdir("../")
        os.chdir("ex0/q0")
        file = open("keywords_intro.txt", "w")
        file.close()
        print("Rendez-vous dans ce répertoire : " + os.getcwd())
        print("Ouvrez le fichier keywords_intro.txt, et entrez-y les mots (1 par ligne) qui vous paraisse obligatoire pour l'introduction de la réponse.")
        input("Appuyez quand c'est fait ...")
        print("Donc, les mots nécessaire pour l'intro sont : \n")
        file = open("keywords_intro.txt", "r")
        line = file.readline()
        while line:
            print("\t" + line)
            line =  file.readline()
        file.close()
E = EVAL()
