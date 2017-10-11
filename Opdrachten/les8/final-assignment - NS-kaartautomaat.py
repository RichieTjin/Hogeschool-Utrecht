def inlezen_beginstation(stations):
    while True:
        beginstation = input('Wat is je beginstation? ')
        for x in stations:
            if beginstation not in x or beginstation == '':
                continue
            else:
                return beginstation

def inlezen_eindstation(stations, beginstation):
    while True:
        eindstation = input('Wat is je eindstation? ')
        for x in stations:
            if eindstation not in x or eindstation == '':
                continue
            else:
                index_beginstation = stations.index(beginstation)
                index_eindstation = stations.index(eindstation)

                if index_eindstation > index_beginstation:
                    return eindstation, index_eindstation, index_beginstation
                else:
                    print('Deze trein komt niet in ' + beginstation)
                    continue


def omroepen_reis(beginstation, eindstation):
    print('Het beginstation ' + str(beginstation) + ' is het ' + str(eindstation[2]) + 'e' + ' station in het traject.')
    print('Het eindstation ' + str(eindstation[0]) + ' is het ' + str(eindstation[1]) + 'e' + ' station in het traject.')

    afstand = eindstation[1] - eindstation[2]

    print('De afstand bedraagt ' + str(afstand) + ' stations(s).')

    prijs = afstand * 5

    print('De prijs van het kaartje is ' + str(prijs) + ' euro.')

stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk','Amsterdam', 'Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', "s-Hertogenbosch", 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht.']
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(beginstation, eindstation)
