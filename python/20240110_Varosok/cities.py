from city import City

cities : list[City] = []

def load_from_file(filename: str) -> bool:
    # try:
        file = open(filename, 'r', encoding='utf-8')
        file.readline()
        for row in file:
            cities.append(City(row))
        file.close()
        return True
    # except Exception as e:
        # print(e)
        # return False

def count_cities_over(population_limit: int) -> int:
    counter = 0
    for c in cities:
        if c.population > population_limit:
            counter += 1
    return counter

def cities_of_highest_population() -> City:
    highest_population_city = cities[0]
    for c in cities:
        if c.population > highest_population_city.population:
            highest_population_city = c
    return highest_population_city

def count_cities_of_country(country: str) ->int:
    counter = 0
    for c in cities:
        if c.country == country:
            counter += 1
    return counter
def sum_pop_country(country: str) ->int:
    sum = 0
    for c in cities:
        if c.country == country:
            sum += c.population
    return sum