# from helsinki import Olimpia

# lista : list[Olimpia] = []

# def load_file(filename) ->None:
#     file = open(filename, 'r', encoding='utf-8')
#     file.readline()
#     for row in file:
#        splitted_data = row.strip().split(' ')
#        lista.append(Olimpia(int(splitted_data[0]), int(splitted_data[1]), splitted_data[2]))
#     file.close
# load_file('helsinki1952.csv')
# print(lista)




# 2. feladat
with open("helsinki.txt", "r") as file:
    data = [line.split() for line in file.readlines()]

# 3. feladat
total_medals = len(data)
print(f"3. feladat: {total_medals} pontszerző helyezés.")

# 4. feladat
placement = data[0]
arany = 0
ezust = 0
bronz = 0
for _, _, placement, _ in data:
    if placement == 1:
        arany += 1
    elif placement == 2:
        ezust += 1
    elif placement == 3:
        bronz += 1

print(f'Arany: {arany}')
print(f'Ezüst: {ezust}')
print(f'Bronz: {bronz}')
# 5. feladat
points = {"1": 7, "2": 5, "3": 4, "4": 3, "5": 2, "6": 1}
total_points = sum(points[placement] for placement, _, _, _ in data)
print(f"5. feladat: Olimpiai pontok összege: {total_points}")


# 6. feladat
medal_counts = {"uszas": 0, "torna": 0}

for _, _, sport, _ in data:
    if sport == "uszas":
        medal_counts["uszas"] += 1
    elif sport == "torna":
        medal_counts["torna"] += 1

winner_sport = max(medal_counts, key=medal_counts.get)
print(f"6. feladat: Az {winner_sport} sportágban szereztek több érmet.")

# 7. feladat
with open("helsinki2.txt", "w") as file:
    for placement, count, sport, _ in data:
        olympic_points = points[placement]
        formatted_sport = sport.replace('_', '-')
        file.write(f"{count} {formatted_sport}: {olympic_points}\n")

# 8. feladat
max_count_data = max(data, key=lambda x: int(x[1]))
max_placement, _, max_sport, max_discipline = max_count_data
print(f'Helyezés: {max_placement}')
print(f'Sportág: {max_sport}')
print(f'Versenyszám: {max_discipline}')
print(f'Sportolók száma: ')
