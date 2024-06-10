class Torna:
    def __init__(self, row: str) -> None:
        splitted = row.strip().split(';')
        self.rajtszam = int(splitted[0])
        self.nev = splitted[1]
        self.orszag = splitted[2]
        self.foldresz = splitted[3]
        self.talaj = float(splitted[4].replace(',' , '.'))
        self.lolenges = float(splitted[5].replace(',' , '.'))
        self.gyuru = float(splitted[6].replace(',' , '.'))
        self.nyujto = float(splitted[7].replace(',' , '.'))
        self.korlat = float(splitted[8].replace(',' , '.'))
        self.ugras = float(splitted[9].replace(',' , '.'))
