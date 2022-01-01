class rectangle:  #creation du classe rectangle 
    def __init__(self,a=0,b=0,c="rectangle"):  #constructeur par defaut 
        self.longueur=a
        self.largeur=b
        self.nom=c

    def display(self): #methode d'affichage
      print(self.longueur, self.largeur , self.nom) 

#exemples 
rect1=rectangle() 
rect2=rectangle(1,2,"recta")
rect1.display()
rect2.display()
#---------------------------------------------------------------------------------------------------------------------
class carre(rectangle):    #creation du classe heritée de la classe precedante 
    
    def _init_(self, a=0, b=0, c="carre"):
        self.longueur=a
        self.largeur=b
        self.nom=c  


    def display(self): #methode d'affichage 
        print("carre")       
        print(self.longueur,self.largeur,self.nom)

#exemples
carre1=carre(2,2,"carre")
rect2=rectangle(1,2,"recta")
carre1.display()
rect2.display()