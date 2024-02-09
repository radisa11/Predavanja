def outer_function(msg):
    message = msg

    def inner_function():
        print(message)

    return inner_function #Vezivanje povratne vrednosti za funkciju

my_function = outer_function("Hi!")
my_function()

def kvadrat():
    print("Kvadrat")

def my_decorator(function_to_decorate):
    def wrapper_around_original_function():
        print("I am a code running before the original function.")

        function_to_decorate()

        print("And i am the code that runs after")

    return wrapper_around_original_function

kvadrat()
my_decorator(kvadrat)()   

@my_decorator
def kub():
    print("kub")

kub()

