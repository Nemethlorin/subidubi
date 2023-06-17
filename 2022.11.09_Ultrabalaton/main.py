from fgvk import *
from Eredmeny import *

eredmenyek = []

FajlOlvas(eredmenyek)
print(f"3.2 feladat: Futók száma: {len(eredmenyek)}")
print(f"3.3 feladat: Célba érkező női sportolók: {GetNoiDb(eredmenyek)} fő")
leghosszabb = GetLeghosszabbNev(eredmenyek)
print(f"3.4 feladat: A leghosszabb nevű futó:")
print(f"\tNév: {leghosszabb.Nev}\n\tRajtszám: {leghosszabb.Rajtszam}\n\tEredmény: {leghosszabb.Ido}")
print(f"3.5 Férfi sportolók átlagos ideje: {GetAtlag(eredmenyek)} óra")