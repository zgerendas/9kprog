import math
import random
'''
egesz = 12
tizedes = 23.67
szoveg = "Szia ékes is lehet!"
logikaiIgaz = True
logikaiHamis = False

print(type(egesz))
print(egesz.bit_length())
# 12 1100

# + - * /
egesz2 = 7
print(egesz + egesz2)
print(egesz - egesz2)
print(egesz * egesz2)
print(egesz / egesz2)

print(type(egesz/1))

print(egesz // egesz2)
print(13 // 12)
print(13 // 11)
print(13 // 5)      # egész osztás

print(13 - 13//5 * 5)
print(13 % 5)      # osztási maradék
print(13 % 11)      

print(3 ** 3)

print(16 ** (1/2))
print(16 ** (0))
print(16 ** (-2))

print(math.sqrt(16))

s = str(egesz)
print(s, egesz)
print(s*10, egesz*10)

#e = int(szoveg)
e = int('123')
print(e,type(e))

#e = int('123*5')
#e = int('12.6')
f = float('12.6')
print(f,type(f))
for i in range(1,10): # [1,10) 
    x=random.random() # [0,1) -> 0 <=x és x <1p
    print(x)
'''
lista = list()
for i in range(1,11): # [1,10) 
    x=random.randint(1,100) # 
    #print(x,end=", ")
    lista.append(x)

print(lista)
print(len(lista))
print(sum(lista))

ment = lista
ment2 = lista.copy()
lista.sort()
print(lista)


print(ment)
print(ment2)
