mondat = ""
while len(mondat) < 10:
    mondat = input("Adja meg a mondatot: ")
mondat = mondat.lower()
mghk = ['a', 'á', 'e', 'é', 'i', 'í', 'o', 'ó', 'ö', 'ő', 'u', 'ú', 'ü', 'ű']
db = 0
for betu in mondat:
    if betu in mghk:
        db+=1
print(f"A magánhangzók száma: {db}")