#creation de la classe 
class Utilisateur:

#membres protegés 
    _nom = "" 
    _email = ""
    _mot_de_passe = ""
    _genre = ""
    _age = 0

    def _init_(self, nom="", email="", mot_de_passe="", genre="", age=0):
        self._nom = nom
        self._email = email
        self._mot_de_passe = mot_de_passe
        self._genre = genre
        self._age = age

    def display(self):
        print(self._nom, "\t", self._email, "\t", self._mot_de_passe, "\t", self._genre, "\t", self._age)

#----------------------------------------------------------------------------------------------------------------------------------
#creation de la classe 
class Module:

#membres privés 
    __nom = 0
    __volume_horaire = 0
    __semestre = ""
    ListMatiere = []
    def _init_(self, nom="", volume_horaire=0, semestre=""):
        self.__nom = nom
        self.__volume_horaire = volume_horaire
        self.__semestre = semestre

    def display(self):
        print(self._nom, "\t", self.volume_horaire, "\t", self._semestre)

#----------------------------------------------------------------------------------------------------------------------------------
#creation de la classe heritée de Utilisateur 
class Professeur(Utilisateur):

#membres privés 
    __ppr = 0
    __grade = ""
    module = Module()
    ListeMatieres = []
    ListeAnnesAcademique = []

    def _init_(self, nom="", email="", mot_de_passe="", genre="", age=0, ppr=0, grade=""):
        super()._init_(self, nom, email, mot_de_passe, genre, age)
        self.__ppr = ppr
        self.__grade = grade

    def display(self):
        print(self._ppr, "\t", self._grade)

#----------------------------------------------------------------------------------------------------------------------------------
#creation de la classe 
class Matiere:

#membres privés 
    __nom = 0
    __pourcentage = 0
    module = Module()
    ListeAnnesAcademique = []
    def _init_(self, nom="", pourcentage=0):
        self.__nom = nom
        self.__pourcentage = pourcentage

    def display(self):
        print(self._nom, "\t", self._pourcentage)

#----------------------------------------------------------------------------------------------------------------------------------
#creation de la classe 
class Annee_Academique:

#membres privés 
    __anne = ""
    Listetudiant = []
    Listematiesre = []
    Listeprofesseur = []

    def _init_(self, anne=""):
        self.__anne = anne

    def display(self):
        print(self.__anne)

#----------------------------------------------------------------------------------------------------------------------------------
#creation de la classe heritée de Utilisateur 
class Etudiant(Utilisateur):

#membres privés 
    __code_massar = ""
    ListAnneAcademique = []

    def _init_(self, nom="", email="", mot_de_passe="", genre="", age=0, code_massar=""):
        super()._init_(nom, email, mot_de_passe, genre, age)
        self.__code_massar = code_massar

    def display(self):
        print(self.__code_massar)

#----------------------------------------------------------------------------------------------------------------------------------
#creation de la classe
class Evaluation:

#membres protegés 
    _note = 0
    matiere = Matiere()
    annee_acadimique = Annee_Academique()
    etudiant = Etudiant()

    def _init_(self, note=0):
        self._note = note

    def display(self):
        print(self._note)