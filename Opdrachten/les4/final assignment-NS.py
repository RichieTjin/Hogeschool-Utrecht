# Final Assignment: NS-functies
# De NS heeft standaardtarieven voor treinreizen, maar onder sommige omstandigheden krijgen
# reizigers korting. Bijvoorbeeld omdat ze in een bepaalde leeftijdscategorie vallen. In deze opdracht
# maak je twee functies: standaardtarief(..) en ritprijs(..). De eerste functie bepaalt het standaardbedrag
# voor een bepaalde rit. De tweede functie maakt hier gebruik van, maar bepaalt zelf ook nog welke
# kortingen van toepassing zijn en levert als return-waarde de definitieve prijs.

# Deel 1: functie standaardprijs
# Schrijf functie standaardprijs(afstandKM). Iedere treinrit kost 80 cent per kilometer, maar als de rit
# langer is dan 50 kilometer betaal je een vast bedrag van €15,- plus 60 cent per kilometer. Ga bij invoer
# van negatieve afstanden uit van een afstand van 0 kilometer (prijs is dan dus 0 Euro).
#

def standaardprijs(afstandKM):
    prijs = 0
    if afstandKM > 50:
        prijs = 15
        prijs += 0.60 * afstandKM
    else:
        prijs = 0.80 * afstandKM
    if prijs != 0:

        return prijs


# Schrijf nu ook de functie ritprijs(leeftijd, weekendrit, afstandKM). De parameter weekendrit is een
# boolean die aangeeft of de rit in het weekend plaats zal hebben (True) of niet (False). Het eerste wat
# de functie ritprijs moet doen, is het aanroepen van de functie standaardprijs, waarbij de afstand in
# kilometers doorgegeven moet worden, om de standaardprijs voor de rit op te vragen. Aan de hand van
# de return-waarde kan de ritprijs worden berekend. De regels zijn als volgt:
# Op werkdagen reizen kinderen (onder 12 jaar) en ouderen (65 en ouder) met 30% korting. In het
# weekend reist deze groep met 35% korting. De overige leeftijdsgroepen reizen betalen de gewone
# prijs, behalve in het weekend, dan reist deze leeftijdsgroep met 40% korting.

# weekendrit = 'true'
#
def ritprijs(leeftijd, weekendrit, afstandKM):
    prijs = standaardprijs(afstandKM)
    if leeftijd < 12 or leeftijd >= 65:
        if weekendrit == 'false':
            ritprijs = (prijs / 100) * 70
            return ritprijs
        else:
            ritprijs = (prijs / 100) * 65
            return ritprijs
    else:
        if weekendrit == 'true':
            ritprijs = (prijs / 100) * 65
            return ritprijs
        else:
            ritprijs = standaardprijs
    return ritprijs

leeftijd = eval(input('Wat is je leeftijd?: '))
weekend = input('Reist u in het weekend: (true or false) ')
afstand = eval(input('Wat is de afstand in km? : '))

print('De prijs voor deze rit bedraagt: ' + str("{0:.2f}".format(ritprijs(leeftijd,weekend,afstand))) + ' euro.')
