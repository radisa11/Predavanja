"""class Auto:
    brzina = 190
    boja = "Crvena"
    agregat = "Dizel"
    broj_mesta = 5

print(Auto.brzina)
print(Auto.boja)
print(Auto.agregat)

jugo = Auto()
print(jugo.boja)
pezo =Auto()"""


class Auto2():
    def __init__(self,br,boja,agregat,broj_mesta) -> None:
        self.brzina = br
        self.boja = boja
        self.agregat = agregat
        self.broj_mesta = broj_mesta 

    def pisi(self):
        print(self.brzina,self.boja,self.agregat,self.broj_mesta)
    
    def vrati_boju(self):
        return self.boja
    
    def postavi_boju(self,nova_boja):
        self.boja = nova_boja



    def __str__(self) -> str:
        return "Osobine su: "+ str(self.brzina)+ " " + self.boja
        

jugo = Auto2(200,"crvena","dizel",6)
jugo.pisi()
print(jugo.boja)
print(jugo.brzina)
print(jugo.vrati_boju())
jugo.postavi_boju("metalic")
print(jugo)


