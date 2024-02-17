class Majka():
    def __init__(self,a):
        self.__a = a

    def pisi(self):
        print(self.__a)

    def promeni(self,a):
        self.__a = a

m = Majka(5)
#print(m.__a) ne moze posto je atribut privatan
m.__a = 7 #ovde se pravi kopija na nivou objekta m
print(m.__a) #ispisuje se kopija i sad prolazi
m.pisi() #ispisuje se ne promenjena vrednost pravog atributa
m.promeni(9) #sada je promenjena vrednost
m.pisi() #ispisuje se promenjena vrednost pravog atributa