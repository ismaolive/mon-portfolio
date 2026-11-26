class Livre:
    
    def __init__(self, titre, auteur, annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
    
    def afficher_details(self):
        print(f"Titre: {self.titre} |  Auteur:{self.auteur} | Anne: {self.annee}")
        
class Bibliotheque:
    def __init__(self):
        self.livres = []
        
    def ajouter_livre(self, livre):
        self.livres.append(livre)
        
    def afficher_catalogue(self):
        print("=== Catalogue de la bibliotheque ===")
        for livre in self.livres:
            livre.afficher_details()
            
livre1 = Livre("Madame Bovary", "Gustave FLAUBERT", 1857)
livre2 = Livre("Les Fleures du mal", "Charles BAUDELAIRE", 1857)
livre3 = Livre("Ny Fiainana Maraine", "JJ.RABEARIVELO", 1924)

bibliotheque = Bibliotheque()
bibliotheque.ajouter_livre(livre1)
bibliotheque.ajouter_livre(livre2)
bibliotheque.ajouter_livre(livre3)

bibliotheque.afficher_catalogue()
                     
               
        
               