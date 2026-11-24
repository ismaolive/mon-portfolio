class Formation:
    def __init__(self, intitule, durree):
        self.intitule = intitule
        self.durree = durree
        
class Etudiant:
    def __init__(self, nom, age, formation):
        self.nom = nom
        self.age = age
        self.formation = formation 
        
    def afficher_informations(self):
        print(f"Etudiant : {self.nom} - Formation : {self.formation.intitule}")
        
athlete_pro = Formation("Athlete Professionnel", 6)

etudiant1 = Etudiant("Harry Kane", 36, athlete_pro)
etudiant1.afficher_informations()
etudiant2 = Etudiant("Lewis Hamilton", 34, athlete_pro)
etudiant2.afficher_informations()
etudiant3 = Etudiant("Kevin Durant", 39, athlete_pro)
etudiant3.afficher_informations()
        
                  