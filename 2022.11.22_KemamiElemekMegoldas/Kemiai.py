from fgvk import *

elemek = []
FajlOlvas(elemek)
print(f"3.feladat: Elemek száma: {len(elemek)}")
print(f"4.feladat: Felfedezések száma az ókorban: {OkorSzamol(elemek)}")
Keres(elemek)
print(f"7.feladat: {MaxKeres(elemek)} év volt a leghosszabb időszak két elem felfedezése között.")
StatKeszit(elemek)