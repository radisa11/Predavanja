name = "global"

def a():
    def b():
        print(name)
    b()

a()

name="global"

def a():
    name="enclosing"   
    def b():
        print(name)
    b()
a()

name="global"

def a():
    name="enclosing"   
    def b():
        name = "local  "
        print(name)
    b()
a()

x = 9
def uvecaj(x):
    x+=1
    return x
x = uvecaj(x)
print(x)









