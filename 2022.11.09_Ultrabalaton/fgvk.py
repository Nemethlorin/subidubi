from Eredmeny import *

def FajlOlvas(eredmenyek):
    f = open("ub2017egyeni.txt", "r", encoding="utf-8")
    f.readline()
    for sor in f:
        eredmenyek.append(Eredmeny(sor))
    f.close()

def GetNoiDb(eredmenyek):
    db = 0
    for eredmeny in eredmenyek:
        if eredmeny.Kategoria == "Noi" and eredmeny.Teljesitett == 100:
            db+=1
    return db

def GetLeghosszabbNev(eredmenyek):
    maxHossz = eredmenyek[0]
    for eredmeny in eredmenyek:
        if len(eredmeny.Nev) > len(maxHossz.Nev):
            maxHossz = eredmeny
    return maxHossz

def GetAtlag(eredmenyek):
    db = 0
    osszeg = 0
    for eredmeny in eredmenyek:
        if eredmeny.Kategoria == "Ferfi" and eredmeny.Teljesitett == 100:
            db+=1
            idoDarabok = eredmeny.Ido.split(':')
            osszeg += int(idoDarabok[0])*3600 + int(idoDarabok[1]) * 60 + int(idoDarabok[2])
    return (osszeg / db) / 3600
