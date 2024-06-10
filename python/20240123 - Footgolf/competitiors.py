from competitor import Competitor
import math

competitors_list : list[Competitor] = []

def load_from_file(filename: str) -> None:
    file = open(filename, 'r', encoding='utf-8')
    for row in file:
        competitors_list.append(Competitor(row))
    file.close()

def count(category: str) -> int:
    counter = 0
    for c in competitors_list:
        if c.category == category:
            counter += 1
    return counter

def winner(category: str) -> Competitor:
    winner_competitor = None
    winner_points = -math.inf
    for c in competitors_list:
        if c.category == category and c.total_points() > winner_points:
            winner_competitor = c
            winner_points = c.total_points()
    return winner_competitor

def save_to_file(filename: str, category: str) -> None:
    file = open(filename, 'w', encoding='utf8')
    for c in competitors_list:
        if c.category == category:
            file.write(f'{c.name};{c.total_points()}\n')
    file.close()