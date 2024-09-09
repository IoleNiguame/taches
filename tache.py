from tkinter import *
import pickle
import time

def day():
    t = time.localtime()
    jour = t[6]
    if jour == 0:
        jour = "lundi"
    elif jour == 1:
        jour = "mardi"
    elif jour == 2:
        jour = "mercredi"
    elif jour == 3:
        jour = "jeudi"
    elif jour == 4:
        jour = "vendredi"
    elif jour == 5:
        jour = "samedi"
    elif jour == 6:
        jour = "dimanche"
    return jour

fichier_donnees1 = open("donnee_tache.dat", "rb")
taches = pickle.load(fichier_donnees1)
fichier_donnees1.close()

tache = taches[day()][0]

root = Tk()
root.minsize(1300, 0)
root.resizable(0, 0)
root.title("Tâches")
root.configure(bg="#E27400")

class Day():
    def __init__(self, day):
        if len(taches[day]) == 1:
            taches[day].append(" ")
        self.tache_dj = "\n".join(taches[day])
        self.frame = Frame(root, relief=SUNKEN, bg="#E27400")
        self.frame.pack(side=LEFT)
        self.lbDay = Button(self.frame, text=day.capitalize(), font=('Arial', 30), width=8, bg="#E2DB00")
        self.lbDay.pack()
        self.lbTache = Label(self.frame, text=self.tache_dj, font=('Arial', 10), bg="#E27400")
        self.lbTache.pack()

frame = Frame(root, bg="#E27400")
labelj = Label(frame, text=day() + " :", font=('Arial', 100), bg="#E27400")
labelj.pack(padx=50)
labelt = Label(frame, text=tache, font=('Arial', 50), bg="#E27400")
labelt.pack()
frame.pack()

def ajouter_tache():
    global btna
    labelj.pack_forget()
    labelt.pack_forget()
    frame.pack_forget()
    btna.pack_forget()
    monday = Day("lundi")
    tuesday = Day("mardi")
    wednesday = Day("mercredi")
    thursday = Day("jeudi")
    friday = Day("vendredi")
    sateday = Day("samedi")
    sunday = Day("dimanche")

btna = Button(text="Ajouter \n des tâches", font=("Arial", 30), bg="#34aa0b", command=ajouter_tache)
btna.pack(fill=X)

#taches = {
#    "lundi" : ["sortir la poubelle noire"],
#    "mardi" : [],
#    "mercredi" : ["sortir la poubelle verte"],
#    "jeudi" : ["il n'y a rien"],s
#    "vendredi" : ["sortir la poubelle noire"],
#    "samedi" : [],
#    "dimanche" : []
#    }
fichier_donnees = open("donnee_tache.dat", "wb")
pickle.dump(taches, fichier_donnees)
fichier_donnees.close()



root.mainloop()
