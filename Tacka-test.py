import Tacka as t

t3 = t.Tacka()
#print(t3.__dict__)
print(t3)
t4 = t.Tacka(1,2)
t5 = t.Tacka(1,2)
print(t4.rastojanje(t5))
print(t4.jednake(t5))
print(id(t4))
print(id(t5))
print(t4 == t5)
print(t4 + t5)