class Majka:


    def __init__(self,a,b) :
        self.__a = a
        self.b = b

    def ispis(self):
        print(f"{self.__a} {self.b}")

    def __str__(self) -> str:
        return f"{self.__a} {self.b}"

    
        
if __name__ == "__main__":
    obj = Majka(9,7)
    print(obj.__dict__)
    print(obj)
    obj.ispis()
    #print(obj.__a)
    print(obj.b)


