class Festmeny:
    def __init__(self, row:str) -> None:
        splitted = row.split().strip()
        self.nev = str(splitted[0])
        self.festo = str(splitted[1])
        self.keszites_eve = int(splitted[2])
        self.ertek = int(splitted[3])
        self.ar = int(splitted[4])
        self.eladas_eve = int(splitted[5])