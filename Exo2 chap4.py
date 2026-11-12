class CompteBancaire:
    
    def __init__(self, titulaire, solde):
        self.titulaire = titulaire
        self.solde = solde
        
    def afficher_solde(self):
        print(f"Titulaire: {self.titulaire}") 
        print(f"Solde disponible: {self.solde}")
     
class CompteEpargne(CompteBancaire):
    
    def __init__(self, titulaire, solde, taux_intérêt):
        super().__init__(titulaire, solde)
        self.taux_intérêt = taux_intérêt
        
    def afficher_solde(self):
        super().afficher_solde()
        print(f"Taux_intérêt: {self.taux_intérêt} %")
        
    def calculer_intérêt(self):
        return self.solde * self.taux_intérêt / 100 
            
compte = CompteEpargne("Miora", 500000, 5)
compte.afficher_solde()
    
print(f"Intérêt: {compte.calculer_intérêt():.0f} Ar")    
        
