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