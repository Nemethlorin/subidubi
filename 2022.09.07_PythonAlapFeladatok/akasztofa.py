import random

szavak = ["alma", "jedlik", "informatika", "számítógép", "hópihe", "kígyó"]
sorszam = random.randint(0, len(szavak)-1)
szo = szavak[sorszam]
betuk = []
for betu in szo:
    betuk.append(betu)
print(szo)

csilaggozott = []
for betu in szo:
    csilaggozott.append("*")
print(f"A szó: {csilaggozott}")

hibaDb = 0
while hibaDb < 3 and "*" in csilaggozott:
    kar = input("Adjon meg egy karaktert: ")
    if kar in betuk:
        for i in range(0, len(betuk)):
            if betuk[i] == kar:
                csilaggozott[i] = kar
    else:
        hibaDb+=1
    kiirtSzo = ""
    for elem in csilaggozott:
        kiirtSzo += elem
    print(f"A szó: {kiirtSzo}")
    print(f"Eddigi hibák: {hibaDb}")

if hibaDb < 3:
    print("Gratulálok! Ön nyert!")
else:
    print("Ön vesztett!")


