class Competitor:
    def __init__(self, row:str) -> None:
        splitted = row.split(';')
        self.name = splitted[0]
        self.category = splitted[1]
        self.team = splitted[2]
        self.points: list[int] = []
        for p in splitted[3:]:
            self.points.append(int(p))

    def min_point(self) -> int:
        mini = 0
        for i in range(len(self.points)):
            if self.points[i] < self.points[mini]:
                mini = i
        return mini

    def min2_points(self) -> int:
        mini = self.min_point()
        if mini == 0:
            mini2 = 1
        else:
            mini2 = 0
        for i in range(len(self.points)):
            if i != mini and self.points[i] < self.points[mini2]:
                mini2 = i
        return mini2

    def total_points(self) -> int:
        mini = self.min_point()
        mini2 = self.min2_points()

        sum_ponits = 0
        for i,p in enumerate(self.points):
            if i != mini and i != mini2:
                sum_ponits += p
        
        if self.points[mini] != 0:
            sum_ponits += 10
        if self.points[mini2] != 0:
            sum_ponits += 10

        return sum_ponits