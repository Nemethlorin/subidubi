rendszamok = ["DYP-803", "YEL-028", "AXU-403", "FOM-220", "TYO-165", "WBZ-322", "GBL-468", "IXH-482", "JCG-896", "EZS-925", "RYR-052", "EPP-310",
        "UTJ-683", "WNA-602", "CJS-123", "DIY-294", "UIZ-581", "OAW-194", "HQI-455", "DKY-950", "PUA-254", "FEB-462", "JGL-218", "KNR-697",
        "MGZ-254", "WXK-680", "RBP-088", "IOU-175", "POI-416", "NJL-604", "QAA-118", "KHW-280", "UGC-233", "LHT-423", "VHF-171", "QAS-607",
        "MNF-037", "JXS-543", "QDQ-505", "QSK-185", "DSO-517", "RHI-930", "VXO-004", "POI-416", "HAW-462", "BFK-791", "QFU-022", "VXI-076",
        "AYH-812", "QYG-277"]

sebessegek = [114.8, 92.386, 71.6, 83.3, 103.4, 87.5, 68.5, 99.7, 94.5, 119.6, 81, 68.3, 87.1, 114, 99.1, 113.7, 102.1, 107.4, 71.4, 85, 85.5,
        104.9, 113.2, 87.9, 114.5, 115.3, 107.9, 81.2, 83.4, 108.1, 81.2, 74.3, 98, 98.1, 89.3, 81.8, 111.3, 80, 71.3, 94.3, 91.6, 108.1,
        85.4, 108.9, 73.3, 67.4, 85.3, 94.6, 95.9, 88.9]

def GetDb():
    db = 0
    for sebesseg in sebessegek:
        if sebesseg > 90:
            db+=1
    return db

def GetUgyanaz():
    tmp = []
    db = 0
    print("2.Feladat: Ugyanazok:")
    for rszam in rendszamok:
        if rszam in tmp:
            print(f"\t{rszam}")
            db+=1
        else:
            tmp.append(rszam)
    print(f"\tÖsszes ismétlődő: {db}")

def GetKulonbseg():
    max = min = sebessegek[0]
    maxIndex = minIndex = 0
    for i in range(len(sebessegek)):
        if max < sebessegek[i]:
            max = sebessegek[i]
            maxIndex = i
        if min > sebessegek[i]:
            min = sebessegek[i]
            minIndex = i
    print(f"3.Feladat:\n\tLeggyorsabb: {rendszamok[maxIndex]} - {max} km/h\n\tLeglassabb: {rendszamok[minIndex]} - {min} km/h\n\tKülönbség: {round(max-min, 2)}")

def GetAtlag():
    ossz = 0
    for sebesseg in sebessegek:
        ossz+= sebesseg
    print(f"4.Feladat: Átlag: {ossz / len(sebessegek)}")

def GetNemleptekAtlag():
    ossz = 0
    db = 0
    for sebesseg in sebessegek:
        if sebesseg <= 90:
            ossz+= sebesseg
            db+=1
    print(f"5.Feladat: Átlag: {ossz / db}")

def BekerKeres():
    beker = input("6.Feladat: Adjon meg egy rendszámot: ")
    for i in range(len(rendszamok)):
        if rendszamok[i] == beker:
            print(f"\t{sebessegek[i]}")
            break

def GetBuntetes():
    buntetesOssz = 0
    for sebesseg in sebessegek:
        if sebesseg > 90 and sebesseg <= 100:
            buntetesOssz+=10000
        elif sebesseg > 100 and sebesseg <= 110:
            buntetesOssz+=15000
        elif sebesseg > 110:
            buntetesOssz+=30000
    print(f"7.Feladat: Összeg {buntetesOssz} Ft")

def GetKorozott():
    for i in range(len(rendszamok)):
        if rendszamok[i][0] == "C" and "123" in rendszamok[i]:
            print(f"8.Feladat: {i+1}.")
            break
        

print(f"1.Feladat: {GetDb()}")
GetUgyanaz()
GetKulonbseg()
print(f"4.Feladat: Átlag: {sum(sebessegek)/len(sebessegek)}")
GetAtlag()
GetNemleptekAtlag()
BekerKeres()
GetBuntetes()
GetKorozott()