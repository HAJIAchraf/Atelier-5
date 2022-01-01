class Point: #creation de la classe point
    def __init__(self, x=0, y=0):    
        self.x1 = x
        self.y1 = y

class Segment: #creation de la classe segment
    def __init__(self, a1, b1, a2, b2):
        self.orig = Point(a1, b1)
        self.extrem = Point(a2, b2)

    def display(self): #methode d'affichage
        print("origine du segment (",self.orig.x1,"," ,self.orig.y1,") extremite (",self.extrem.x1,"," ,self.extrem.y1,")")

#exemple 
segment1 = Segment(1, 2, 3, 4)
segment1.display()