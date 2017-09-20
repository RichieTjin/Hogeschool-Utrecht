# Schrijf (en test) functie wijzig() met één parameter: letterlijst. Zorg dat de functie de lijst leegt en de
# letters [ ‘d’, ‘e’, ‘f’ ] toevoegt. Er is geen return-waarde! Test je programma als volgt:
# lijst = ['a', 'b', 'c']
# print(lijst)
# wijzig(lijst)
# print(lijst)
# Uitvoer:
# ['a', 'b', 'c']
# ['d', 'e', 'f']

letterlijst = ['a', 'b', 'c']

def wijzig(letterlijst):
    letterlijst = ['d', 'e', 'f']
    print(letterlijst)


# • Waarom kun je in de functie niet de opdracht lijst = ['d', 'e', 'f'] geven?
#   ?

# • Werkt jouw functie ook met een string-parameter? Probeer dit! Waarom werkt het wel/niet?
letterlijst = ['a', 'b', 'c']

def wijzig(letterlijst):
    letterlijst = str(['d', 'e', 'f'])
    print(letterlijst)
#     Er gebeurd niks.

# • Welke rol speelt (im)mutabiliteit in deze vraag?
#   ?