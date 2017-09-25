# Schrijf (en test) functie wijzig() met één parameter: letterlijst. Zorg dat de functie de lijst leegt en de
# letters [ ‘d’, ‘e’, ‘f’ ] toevoegt. Er is geen return-waarde! Test je programma als volgt:
# lijst = ['a', 'b', 'c']
# print(lijst)
# wijzig(lijst)
# print(lijst)
# Uitvoer:
# ['a', 'b', 'c']
# ['d', 'e', 'f']

def wijzig(letterlijst):
    letterlijst.clear()
    letterlijst.append('d')
    letterlijst.append('e')
    letterlijst.append('f')

letterlijst = ['a', 'b', 'c']
print(letterlijst)
wijzig(letterlijst)
print(letterlijst)


# • Waarom kun je in de functie niet de opdracht lijst = ['d', 'e', 'f'] geven?
def wijzig(letterlijst):
    letterlijst = ['d', 'e', 'f']

letterlijst = ['a', 'b', 'c']
print(letterlijst)
wijzig(letterlijst)
print(letterlijst)
#   Omdat de functie de parameter wel veranderd maar er verder niks mee doet.


# • Werkt jouw functie ook met een string-parameter? Probeer dit! Waarom werkt het wel/niet?
def wijzig(letterlijst):
    letterlijst.clear()
    letterlijst.append('d')
    letterlijst.append('e')
    letterlijst.append('f')

letterlijst = ['adddddevtrgt']
print(letterlijst)
wijzig(letterlijst)
print(letterlijst)
# Hij doet het wel.

# • Welke rol speelt (im)mutabiliteit in deze vraag?
#   ?