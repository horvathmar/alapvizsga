class Iranyitok:
    def __init__(self, row: str):
        splitted = row.strip().split(';')
        self.nev = splitted[0]
        self.passzolt_yardok = int(splitted[1])
        self.pass_kiserletek = int(splitted[2])
        self.sikeres_passzok = int(splitted[3])
        self.td_passzok = int(splitted[4])
        self.eladott_labdak = int(splitted[5])
        self.iranyito_mutato = splitted[6]
        self.egyetem = splitted[7]
        splittelt = self.iranyito_mutato.split(',')
        self.mutato_elso_szam = int(splittelt[0])
        self.passzolt_yardok_meterre = round(self.passzolt_yardok * 0.9144)