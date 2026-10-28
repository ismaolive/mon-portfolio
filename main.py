class Personne:
    def __init__(self, nom, age, adresse, situation_familiale):
        self.nom = nom
        self.age = age
        self.adresse = adresse
        self.situation_familiale = situation_familiale
        self.statut = "En attente de confirmation"

    def demander_aide(self):
        print(self.nom, "demande une aide sociale.")

    def afficher_informations(self):
        print("Nom :", self.nom)
        print("Âge :", self.age)
        print("Adresse :", self.adresse)
        print("Situation familiale :", self.situation_familiale)
        print("Statut :", self.statut)


personne1 = Personne("Zorza", 27, "Antananarivo", "Célibataire")

personne1.demander_aide()
personne1.afficher_informations()

    