# eljárások, függvények

def sorminta():
    print('*'*20)
    print('-'*10)
    print('*'*20)

# sorminta()
# sorminta()
'''
s = "12"
print(s.isalnum())
s = "12.5"
print(s.isalnum())
s = "a12"
print(s.isalnum())

s = "12"
print(s.isdecimal())
s = "12.5"
print(s.isdecimal())
s = "a12"
print(s.isdecimal())




def beEgesz():
    szam = input("Kérek egy egész számot: ")
    if szam.isdecimal():
        return int(szam)
    else:
        return beEgesz()
    

print(beEgesz()*2)

def beEgesz2(kezd,veg):
    szam = input("Kérek egy egész "+str(kezd)+" és "+str(veg)+" közötti számot: ")
    
    if szam.isdecimal():
        if kezd <= int(szam) and int(szam) <= veg:
            return int(szam)
        else:
            print("Nincs a ",kezd," és a",veg," között a szám!")
            return beEgesz2(kezd,veg)
    else:
        print("Nem egész számot írtál be!")
        return beEgesz2(kezd,veg)

print(beEgesz2(1,100))


sz = int(input("Kérek egy egész számot: "))
print(sz*2)

'''

def nagyobb(x,y):
    if x > y:
        return x
    else:
        return y

print(nagyobb(23,6))
print(nagyobb(1.423,-6))


def negativ(szam):
    if szam < 0:
        return True
    else:
        return False
    
    #return szam < 0

print(negativ(12))  # -> False
print(negativ(-12)) # -> True




