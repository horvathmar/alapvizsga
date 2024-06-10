class Kuldetesek:
    def __init__(self, row: str) -> None:
        splitted = row.strip().split(';')
        self.kod = splitted[0]
        self.datum = splitted[1]
        self.nev = splitted[2]
        self.napok_szama = int(splitted[3])
        self.orak_szama = int(splitted[4])
        self.tamaszpont_neve = splitted[5]
        self.legenyseg_szama = int(splitted[6])
        darabolt_datum = self.datum.split('.')
        self.ev = int(darabolt_datum[0])
        self.ossz_ora = (self.napok_szama *24) + self.orak_szama