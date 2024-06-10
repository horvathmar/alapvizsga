class City:
    def __init__(self, row:str) -> None:
        #Bengaluru;India;8443675
        splitted = row.split(';')
        self.name = splitted[0]
        self.country = splitted[1]
        self.population = int(splitted[2])