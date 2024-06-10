class Prize:
    def __init__(self, row: str) -> None:
        splitted = row.split(';')
        self.year = int(splitted[0])
        self.type = splitted[1]
        self.firstname = splitted[2]
        self.latsname = splitted[3]
        self.full_name = self.latsname + ' ' + self.firstname