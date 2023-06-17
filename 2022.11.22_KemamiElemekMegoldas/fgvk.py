from Elem import *

def FajlOlvas(elemek):
    f = open("felfedezesek.txt", "r", encoding="utf-8")
    f.readline()
    for sor in f:
        elemek.append(Elem(sor))
    f.close()

def OkorSzamol(elemek):
    db = 0
    for elem in elemek:
        if elem.Ev == "Ókor":
            db+=1
        else:
            return db

def BetuCheck(beker):
    for i in range(len(beker)):
        if not ((beker[i] >= "A" and beker[i] <= "Z") or (beker[i] >= 'a' and beker[i] <= 'z')):
            return False
    return True

def Beker():
    beker = ""
    while len(beker) != 1 and len(beker) != 2 or not BetuCheck(beker):
        beker = input(f"5.feladat: Kérek egy vegyjelet: ")
    return beker

def Keres(elemek):
    beker = Beker()
    print("6. feladat: Keresés:")
    for elem in elemek:
        if elem.Vegyjel.lower() == beker.lower():
            print(f"\tAz elem vegyjele: {elem.Vegyjel}\n\tAz elem neve: {elem.Nev}\n\tRendszáma: {elem.Rendszam}\n\tFelfedezés éve: {elem.Ev}\n\tFelfedező: {elem.Felfedezo}")
            break

def MaxKeres(elemek):
    max = 0
    for i in range(0, len(elemek)-1):
        if elemek[i].Ev != "Ókor":
            kulonbseg = int(elemek[i+1].Ev) - int(elemek[i].Ev)
            if kulonbseg > max:
                max = kulonbseg
    return max

def StatKeszit(elemek):
    stat = {}
    for elem in elemek:
        if elem.Ev != "Ókor":
            if elem.Ev in stat.keys():
                stat[elem.Ev] += 1
            else:
                stat[elem.Ev] = 1
    print("8.feladat:")
    for key, value in stat.items():
        if value > 3:
            print(f"\t{key}: {value} db")


