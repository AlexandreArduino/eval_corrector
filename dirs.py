import os

class DIRECTORIES(object):
    def __init__(self):
        self.path = os.getcwd()
        print("+ dirs.py")
        print("\t- Chemin définie pour l'utilisation du logiciel : " + self.path)
        print("\t- Sauvegarde de celui-ci ...")
        try:
            file = open("data/path.cfg", "w")
            file.write(self.path)
            file.close()
        except:
            self.warning("Le dossier data n'est pas présent. Si c'est votre première utilisation pas de problèmes sinon, vos données ont été perdues :/")
            print("\t- Création du dossier data dans " + self.path + "/data")
            os.mkdir("data")
            print("\t- Dossier créé !\n\t- Sauvegarde du chemin ...")
            file = open("data/path.cfg", "w")
            file.write(self.path)
            file.close()
            try:
                del file
            except:
                self.warning("Impossible de supprimer file de la RAM")
        self.define_os()
        self.wait_for_continue()
    def warning(self, text):
        print("\t- /!\ WARNING : " + text)
        try:
            del text
        except:
            pass
    def define_os(self):
        print("\t- Recherche du système d'exploitation ...")
        self.os = os.name
        if self.os == "posix":
            self.os = "linux"
        elif self.os == "nt":
            self.os = "windows"
        else:
            self.os = "undefined"
        print("\t- Résultat de la recherche : " + self.os)
        print("\t- Sauvegarde de la recherche ...")
        file = open("data/os", "w")
        file.write(self.os)
        file.close()
        try:
            del file
        except:
            self.warning("Impossible de supprimer la variable file de la RAM")
    def clear(self):
        if self.os == "linux":
            os.system('clear')
        elif self.os == "windows":
            os.system('cls')
        else:
            self.warning("Impossible de vider l'écran, système d'exploitation non défini.")
    def wait_for_continue(self):
        input("\n\nAppuyez pour démarrer ...")
        self.clear()
D = DIRECTORIES()
