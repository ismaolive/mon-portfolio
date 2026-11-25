class Produit:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix
        
class Commande:
    def __init__(self, produit, quantite):
        self.produit = produit 
        self.quantite = quantite
        
    def calculer_total(self):
        return self.produit.prix * self.quantite  
    
    def afficher_commande(self):
        print("Produit:", self.produit.nom)  
        print("Quantite:", self.quantite)
        print("Total:", self.calculer_total())    
        
produit1 = Produit("Poudre Magic", 8000)
produit2 = Produit("Liquide vaisselle", 6500)
produit3 = Produit("Machine Coupante", 150000)


commande1 = Commande(produit1, 4)
commande2 = Commande(produit2, 6)
commande3 = Commande(produit3, 1)

print("Total commande1:", commande1.calculer_total())
print("Total commande2:", commande2.calculer_total())
print("Total commande3:", commande3.calculer_total())

commande1.afficher_commande()
commande2.afficher_commande()
commande3.afficher_commande()