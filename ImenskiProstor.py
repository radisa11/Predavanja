x = 9
def fun(c):
    b =3
    x = 7
    print(x)
    def fun2():
        pass
    locals()["b"] = 90
    print(locals())
    print(locals()["b"])

fun(0)
print(x)
print("-------------------")
globals()["x"] = 19
print(globals())


