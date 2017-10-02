# Gegeven is variabele invoer = "5-9-7-1-7-8-3-2-4-8-7-9". Schrijf een nieuw programma
# waarin je deze variabele splitst in een lijst van getallen en print de gesorteerde lijst. Bepaal en print na
# het opsplitsen de grootste waarde, kleinste waarde, aantal getallen, de som en het gemiddelde!

def split(invoer):
    alles = invoer.split('-')

    nieuw_alles = []
    for num in alles:
        nieuw_alles.append(int(num))

    grootste_getal = max(alles)
    print('grootste waarde: ' + grootste_getal)

    kleinste_getal = min(alles)
    print('kleinste waarde: ' + kleinste_getal)

    aantal = str(len(alles))
    print('aantal: ' + aantal)

    som = str(sum(nieuw_alles))
    print('totaal: ' + som)

    berekening = int(som) / int(aantal)
    gemiddelde = ('gemiddelde: ' + str(berekening))

    return gemiddelde


print(split("5-9-7-1-7-8-3-2-4-8-7-9"))