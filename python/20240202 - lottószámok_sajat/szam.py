class Szamok:
    def __init__(self, row: str) -> None:
        splitted = row.split(' ')
        self.szamok = []
        for szam in splitted:
            self.szamok.append(int(szam))