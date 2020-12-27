'''from tkinter import *

class EVAL_CORRECTOR_APP(object):
    def __init__(self):
        self.app = Tk()
        self.app.title("Eval Corrector, projet open source développé en Python par BAALBAKYA")
        self.title = Label(self.app, text="Eval Corrector", font=("Courrier", 30))
        self.label_eval_name = Label(self.app, text="Nom de l'évaluation : ", font=("Courrier", 10))
        self.label_eval_name.place(x = 100,y = 0)
        self.title.pack()
        self.label_eval_name.pack()
        self.app.mainloop()
E = EVAL_CORRECTOR_APP()'''

import os
from time import sleep
from random import randint

class APP(object):
    def __init__(self):
        file = open("data/os", "r")
        self.os = file.readline()
        file.close()
        self.title_screen()
    def clear(self):
        if self.os == "linux":
            os.system('clear')
        elif self.os == "windows":
            os.system('cls')
        else:
            pass
    def title_screen(self):
        title = list("EVAL CORRECTOR OPEN SOURCE PROJECT IN PYTHON")
        for i in range(len(title)):
            self.clear()
            print("".join(title[:i]))
            sleep(i/200)
        self.clear()
        print("".join(title))
        del i
        text = ""
        for i in range(50):
            text += "#"
            self.clear()
            print("".join(title))
            print(text)
            print("Projet développé par BAALBAKYA ...")
            sleep(randint(0, 100)/500)
        self.clear()
        file = open("data/logo.bt", "r")
        line = file.readline()
        l = []
        while line:
            self.clear()
            print("".join(title))
            print(text)
            l.append(line)
            for i in range(0, len(l)):
                print(l[i])
            sleep(randint(0, 100)/500)
            line = file.readline()
        file.close()
        for j in range(0, 33):
            self.clear()
            print("".join(title))
            print(text)
            for p in range(0, j):
                print("")
            l.append(line)
            for i in range(0, len(l)):
                print(l[i])
            sleep(.1)
        input("Appuyez pour commencer ...")
A = APP()
