'''
v = 1,2,3
print(v)
print(type(v))

l = list()
l.append(1)
l.append("alma")
print(l)
print(type(l))

t = (1,2,3,"pipacs")
print(t,type(t))

halmaz = {1,2,3,"alma"}
print(halmaz,type(halmaz))

l = [1,2,3,3,4]
t = (1,2,3,3,4)
h = {1,2,3,3,4}

print(l,t,h,sep="\n")

l.append(t)
print(l)
h.add(t)
print(h)

l.append(h)
print(l)

#h.add(l)
#print(h)
'''

szoveg = "alma Nisi Minim ut laboris aliquip aliqua dolor proident consequat aliqua alma."
print(szoveg.capitalize())
print(szoveg.count("a"))
print(szoveg.count("alma"))
print(szoveg.count("á"))

lista = szoveg.split(" ")
print(lista)
print(lista.count("alma"))

print(szoveg.find("ma"))
print(szoveg.find("ma"))
print(szoveg.find("ma",3))

print(lista.index("ut"))
print(lista[0])
print("Lista elem száma:",len(lista))   #
print("Szöveg karaktereinek száma:",len(szoveg))  # 

print(lista[len(lista)-1])
print(lista[-1])
print(lista[-2])
print(szoveg[-1])


