class etudiant: #creation de la classe etudiant
    def __init__(self, nom, prenom, age, cne, moyenne):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.cne = cne
        self.moyenne = moyenne

liste = [
        etudiant("haji", "achraf",21 , "P148003025", 12),
        etudiant("achraf", "haji", 21, "A148003025", 13),
        etudiant("test", "test1", 21, "A148003025", 11),
        etudiant("test2", "test3", 21, "A148003025", 15)
        ]

