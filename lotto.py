import random

huzott = random.randint(1,91) 
# huzott = [kezd,veg) -> kezd <= huzott < veg

h1 = random.randint(1,91) 
h2 = random.randint(1,91) 
# ...

szamok = list()
for i in range(5):
    szamok.append(random.randint(1,91) )
print(szamok)


szamok = set()
for i in range(5):
    szamok.add(random.randint(1,91) )
print(szamok)
print("*"*20)
for i in range(52):
    szamok.clear()
    while len(szamok) < 5:
        szamok.add(random.randint(1,91) )
    print(szamok)
