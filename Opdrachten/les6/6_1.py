# Schrijf een functie seizoen(maand) die als parameter maandnummer meekrijgt. Het functie-resultaat
# is het seizoen die bij die maand hoort. Nummers 3 t/m 5 horen bij lente, 9 t/m 11 ‘herfst’ etc.

def seizoen(maand) ->int:
    if maand >= 3 and maand < 6:
        print('lente')
    elif maand >= 6 and maand < 9:
        print('zomer')
    elif maand >= 9 and maand < 12:
        print('herfst')
    else:
        print('winter')
seizoen(11)