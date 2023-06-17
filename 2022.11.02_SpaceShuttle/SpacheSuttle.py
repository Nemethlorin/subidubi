from fuggvenyek import *

kuldetesek = []

FajlBeolvas(kuldetesek)
print(f"3.Feladat:\n\tÖsszesen {len(kuldetesek)} alkalommal indítottak űrhajót!")
print(f"4.Feladat:\n\t{GetUtasSzam(kuldetesek)} utas indult az űrbe összesen.")
print(f"5.Feladat:\n\tÖsszesen {GetOtnelKevesebb(kuldetesek)} alkalommal küldtek kevesebb, mint 5 embert az űrbe.")
print(f"6.Feladat:\n\t{GetColumbiaLegenyseg(kuldetesek)} asztronauta volt a Columbia fedélzetén annak utolsó útján")
legKuldetes = GetLeghosszabb(kuldetesek)
print(f"7.Feladat:\n\tA leghosszabb ideig a {legKuldetes.UrsikloNev} volt az űrben a {legKuldetes.Kod} küldetés során\n\tÖsszesen {legKuldetes.IdoOraban()} órát volt távolt a Földtől.")