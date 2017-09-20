# Schrijf een programma dat de gebruiker vraagt om zijn uurloon, het aantal uur dat hij of zij gewerkt
# heeft en dat daarna het salaris uitprint.

# Voorbeelduitvoer:
# Wat verdien je per uur: 3.80
# Hoeveel uur heb je gewerkt: 20
# 20 uur werken levert 76.0 Euro op

uurloon = input('wat verdien je per uur: ')
uren = input('hoeveel uur heb je gewerkt: ')

totaal = int(uurloon) * int(uren)

print(uurloon + 'uur werken levert: ' + str(totaal) + ' euro op')

