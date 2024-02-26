# 1
knev = input("Kérem a keresztneved: ")
vnev = input("Kérem a vezeték neved: ")
teljes_nev = vnev + " " + knev
print("Üdvözöllek " + teljes_nev)

# 2
szam = float(input("Kérek egy számot: "))
szerencse_szam = (szam*2+3 )/2
print("A szerencse számod:",szerencse_szam)

# 3
egesz = 12
tizdes = 2.05
szoveg = "Valami"
logikai = True
lista =[1,2,3]
halmaz = {1,2,2,3}
tupple = ('a','b') 

print("Egész:",egesz)
print("Tizedes:",tizdes)
print("Szöveg:",szoveg)
print("Logaikai:",logikai)
print("Lista:",lista)
print("Halmaz:",halmaz)
print("Tuple:",tupple)

# 4
import random

szamok = list()
for i in range(5):
    szamok.append(random.randint(1,7))

tipp = int(input("Kérek egy egész számot 1 és 7 között: "))
if tipp in szamok:
    print("A szám a listában volt.")
else:
    print("A szám nincs a listában.")
print("A lista: ",end="")

for i in szamok:
    print(i,end=", ")
print()

# 5 
def addSzor(a,b):
    return (a+b)*2
print("Eredmény: 2,3 ->",addSzor(2,3))