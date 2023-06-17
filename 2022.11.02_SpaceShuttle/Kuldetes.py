import datetime

class Kuldetes:
    def __init__(self, sor):
        adatok = sor.strip().split(';')
        datumdb = adatok[1].split('.')
        self.Kod = adatok[0]
        self.KilovesDatum = datetime.datetime(int(datumdb[0]), int(datumdb[1]), int(datumdb[2]))
        self.UrsikloNev = adatok[2]
        self.Nap = int(adatok[3])
        self.Ora = int(adatok[4])
        self.Landolt = adatok[5]
        self.Legenyseg = int(adatok[6])

    def IdoOraban(self):
        return self.Nap*24 + self.Ora
