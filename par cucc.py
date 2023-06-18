kajak = ["alma", "körte", "banan","körte","körte","alma","alma","alma"]
stat  = {}
for  kaja in kajak:
    if(stat.get(kaja)) == None:
        stat[kaja] = 1
    else:
        stat[kaja] += 1
for key, value in stat.items():
        print(f"{key}-bol {value} db van")


import math

while True:
    try:
        u = float(input("u="))
        a = float(input("a="))
        s = float(input("s="))
        v = u + math.sqrt(2*a*s)
        print(f"v={v:.2f}")
        break
    except:
        print("A bevitt adatok valamelyike hibás!")