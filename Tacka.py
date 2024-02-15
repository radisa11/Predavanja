import math

class Tacka:
    def __init__(self,x=0,y=0) -> None:
        self.x = x
        self.y = y

    def kopiraj(self,t):
        self.x = t.x
        self.y = t.y

    def jednake(self,t):
        """if self.x == t.x and self.y == t.y:
            return True
        return False"""
        if isinstance(t,Tacka):
            return self.x == t.x and self.y == t.y
        return False
    
    def __eq__(self,t):
        print("poziva se equal")
        if isinstance(t,Tacka):
            return self.x == t.x and self.y == t.y
        return False
    
    def __add__(self,t):
        return Tacka(self.x + t.x, self.y + t.y)


    def rastojanje(self,t):
        return math.sqrt((t.x-self.x)**2+(t.y-self.y)**2)
    
    def __str__(self) -> str:
        return f"({self.x},{self.y})"
    
if __name__ == "__main__":
    t1 = Tacka()
    print(t1.__dict__)
    t2 = Tacka(3,4)
    print(t2.__dict__)
    print(t2)
    t1.kopiraj(t2)
    print(t1)