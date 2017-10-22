def bereken():
    aantal_personen = input('Hoeveel personen? ')
    bedrag = input('Wat is het totaal bedrag? ')

    while True:
        try:
            int(bedrag)
            int(aantal_personen)
        except ValueError:
            print('Gebruik cijfers voor het invoeren van het aantal/bedrag')
            break
        if aantal_personen == 0:
            print('Delen door nul kan niet')
            break
        elif int(aantal_personen) < 0:
            print('Negatieve getallen zijn niet toegestaan')
            break
        else:
            bedrag_pp = int(bedrag) / int(aantal_personen)
            print(bedrag_pp)
            break

bereken()