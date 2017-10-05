groene_lijn = set(['Boxtel', 24, 'Beukenlaan', 'Eindhoven', 'Geldrop', 'Heeze', 25, 'Weert'])
bruine_lijn = set(['Boxtel', 'Best', 27, 'Eindhoven', "Helmond 't Hout", 'Helmond', 'Helmond Brouwhuis', 'Deurne'])

print(groene_lijn.intersection(bruine_lijn))

print(bruine_lijn.difference(groene_lijn))

print(groene_lijn.union(bruine_lijn))