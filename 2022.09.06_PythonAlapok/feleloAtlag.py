db = int(input("Adja meg a felelések számát: "))
atlag = 0
for i in range(0,db):
    atlag += random.randint(1,5)
print(f"Átlag: {atlag/db}")
atlag = atlag/db

szovJegy = ""

if atlag <= 1.5:
    szovJegy = "Elégtelen"
elif atlag > 1.5 and atlag < 2.5:
    szovJegy = "Elégséges"
elif atlag >= 2.5 and atlag < 3.5:
    szovJegy = "Közepes"
elif atlag >= 3.5 and atlag < 4.5:
    szovJegy = "Jó"
else:
    szovJegy = "Jeles"
print(f"Az érdemjegy: {szovJegy}")