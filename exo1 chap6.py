class Moteur:
    def __init__(self, marque, puissance):
        self.marque = marque
        self.puissance = puissance
        
    def demarrer(self):
        print(f"Le moteur {self.marque} de {self.puissance} ch démarre.")
            
class Voiture:
    def __init__(self, marque_moteur, puissance):
        self.moteur = Moteur(marque_moteur, puissance) 
    
    def demarrer(self):
        print("La voiture démarre...")
        self.moteur.demarrer()
        
ma_voiture = Voiture("Ford", 1000)
ma_voiture.demarrer()         
