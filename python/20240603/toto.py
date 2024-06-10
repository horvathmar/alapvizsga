class Totok:
    def __init__(self, row: str) -> None:
        splitted = row.strip().split(';')
        self.ev = int(splitted[0])
        self.het = int(splitted[1])
        self.fordulo = int(splitted[2])
        self.t13p1 = int(splitted[3])
        self.ny13p1 = int(splitted[4])
        self.eredmenyek = splitted[5]