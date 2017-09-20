# Schrijf (en test) de functie lang_genoeg() die voor Efteling-attracties bepaalt of een gebruiker in een
# attractie mag. De functie heeft één parameter, namelijk de lengte van de gebruiker in centimeters. Als
# de gebruiker 120 centimeter of langer is de return-waarde van de functie “Je bent lang genoeg voor
# de attractie!”, anders is de melding “Sorry, je bent te klein!”.

def lang_genoeg(lengte):
    if lengte >= 120:
        print('je bent lang genoeg voor de attractie!')
    else:
       print('sorry je bent te klein')

lang_genoeg(120)