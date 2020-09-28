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
            #en dehors des questions

        '''
        ex1 => 1q
        q :
        1 phrase d'intro => avec des mots clés
        calcul => la formule, les valeurs, et le résultat
        la phrase outro => mots clés
        '''
E = EVAL()
