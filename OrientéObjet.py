class Etudiant():
    def __init__(self, e_nom, e_prenom, ):
        self.nom = e_nom
        self.prénom = e_prenom
        self.notes = []

    def Moyenne(self):
        return sum(self.notes)/len(self.notes)

    def AfficherMoyenne(self):
        if len(self.notes) == 0:
            print(f"l'élèves {self.prénom} n'a pas encore eu de notes")
        else:
            print(f"l'élève {self.nom} a pour moyenne {self.Moyenne()}")


Etudiant_Yann = Etudiant('Sko', 'Yann')
Etudiant_Yann.AfficherMoyenne()
Etudiant_Yann.notes.append(18)
Etudiant_Yann.AfficherMoyenne()
Etudiant_Yann.notes.append(12)
Etudiant_Yann.notes.append(15)
Etudiant_Yann.AfficherMoyenne()
