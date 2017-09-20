# Schrijf (en test) de functie som() die 1 parameter heeft: getallenLijst. Ga ervan uit dat dit een list is
# met integers. De return-waarde van de functie moet de som (optelling) van de getallen in de lijst zijn!
# Tip: bekijk nog eens de list-functies (Perkovic, blz. 28).

getallenlijst = [345,2345,456,345,2,4,53,456]

def som(getallenlijst):
    total = sum(getallenlijst)
    print(total)

som(getallenlijst)