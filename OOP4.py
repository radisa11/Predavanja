class Person:
    origin_country = "USA"
    def __init__(self,name, age,gender) -> None:
        self.name = name
        self.age = age
        self.gender = gender

    @classmethod
    def metoda(cls,zemlja):
        cls.origin_country = zemlja

    @staticmethod
    def metod2():
        print("Bilo sta")


    def speak(self,words):
        print(f"{self.name} speaks {words}")

ana = Person("Ana Petrovic",30,"F")
ana.speak("Zdravo")
print(ana.origin_country)
print(Person.origin_country)
print(ana.name)
Person.metoda("Srbija")
print(Person.origin_country)
Person.metod2()
ana.metod2()