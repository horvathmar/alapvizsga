from prizes import *

load_file('nobel.csv')
print_all_names()
result = search_by_name('Arthur B. McDonald')
if result == None:
    print('Nincs ilyen díjazott')
else:
    print(f'Arthur B. McDonald {result.type} díjat kapott')

result = search_by_year_and_type(2017, 'irodalmi')
if result == None:
    print('2017 évben nincs irodalmi díjazott')
else:
    print(f'2017-ben irodalmi Nobel_díjat kapott: {result.full_name}')

print('1990 után béke Nobel_díjat kaptak az alábbi szervezetek: ')
for p in search_organisation_by_type_from('béke', 1990):
    print(f'\t {p.firstname}')

print()
curie_van()