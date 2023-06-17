from Kuldetes import *

def FajlBeolvas(lista):
    f = open("kuldetesek.csv", "r", encoding="utf-8")
    for sor in f:
        egyKuldetes = Kuldetes(sor)
        lista.append(egyKuldetes)
    f.close()

def GetUtasSzam(lista):
    ossz = 0
    for kuldetes in lista:
        ossz += kuldetes.Legenyseg
    return ossz

def GetOtnelKevesebb(lista):
    db = 0
    for kuldetes in lista:
        if kuldetes.Legenyseg < 5:
            db+=1
    return db

def GetColumbiaLegenyseg(lista):
    for kuldetes in lista:
        if kuldetes.UrsikloNev == "Columbia" and kuldetes.Landolt == "nem landolt":
            return kuldetes.Legenyseg
    return 0

def GetLeghosszabb(lista):
    maxKuldetes = lista[0]
    for kuldetes in lista:
        if kuldetes.IdoOraban() > maxKuldetes.IdoOraban():
            maxKuldetes = kuldetes
    return maxKuldetes