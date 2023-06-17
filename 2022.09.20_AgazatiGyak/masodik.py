from operator import truediv


def GetSzokoEvek():
    evek = []
    nagyobb = 0
    kisebb = 0
    if evszam1 > evszam2:
        nagyobb = evszam1
        kisebb = evszam2
    else:
        nagyobb = evszam2
        kisebb = evszam1
    for evszam in range(kisebb, nagyobb+1):
        if CheckEv(evszam):
            kisebb = evszam
            break
    for evszam in range(kisebb, nagyobb+1, 4):
        if CheckEv(evszam):
            evek.append(evszam)
    return evek
    
def CheckEv(ev):
    if ev % 400 == 0 or (ev % 4 == 0 and ev % 100 > 0):
        return True
    return False

print("2. feladat: Szökőév listázó")
evszam1 = int(input("Kérem az egyik évszámot: "))
evszam2 = int(input("Kérem a második évszámot: "))
evekLista = GetSzokoEvek()
if len(evekLista) == 0:
    print("Nincs szökőév a megadott tartományban!")
else:
    eredmeny = "Szökőévek:"
    for evszam in evekLista:
        eredmeny+= f"{evszam}; "
    print(eredmeny[:-2])