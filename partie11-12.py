class vecteur2D:
    def __init__(self, x0=0, y0=0):  #constructeur parametre
        self.x = x0 
        self.y = y0

    def display(self):  #methode d'affichage
        print(self.x,self.y)

    def addition(self,other):  #methode pour calculer l'addition
        x=self.x+other.x
        y=self.y+other.y
        print("le resultat est (",x,y,")")

vect1=vecteur2D() #exemple1
vect2=vecteur2D(3,4) #exemple2
vect3=vecteur2D(5,6) #exemple3
print("Constructeur par defaut : ")
vect1.display() #affichage de l'exemple 1 costruit par defaut
print("Constructeur parametre : ")
vect2.display() #affichage de l'exemple 2 
print("addition vect1 + vecr2 : ")
vect3.addition(vect2) #affichage de l'addition du l"exemple 2 et 3 

