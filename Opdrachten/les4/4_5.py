# Schrijf (en test) de functie kwadraten_som() die 1 parameter heeft: grondgetallen. Dit is een list is
# met integers. De return-waarde van de functie is de som van de kwadraten van alle positieve getallen
# in de lijst! Een lijst van [ 4, 5, 3, -81 ] heeft als return-waarde dus 50 (16 + 9 + 25).

grondgetallen = [4, 5, 3, -81]

def kwadraten_som(grondgetallen):
    for getal in grondgetallen:
        if getal >= 0:
            kwadraat = getal ** 2
            print(kwadraat)

kwadraten_som(grondgetallen)