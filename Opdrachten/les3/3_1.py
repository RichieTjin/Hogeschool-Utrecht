# Schrijf een programma dat de gebruiker vraagt om de score van een multiplechoice toets. Het
# programma bepaalt of het resultaat voldoende is. Bij meer dan 15 punten is de deelnemer geslaagd!

# Voorbeelduitvoer:
# Geef je score: 18
# Gefeliciteerd!
# Met een score van 18 ben je geslaagd!

# Waarschijnlijk heb je de bovenstaande uitvoer geprogrammeerd met 2 print()-opdrachten. Wat
# gebeurt er als je de tweede print()-opdracht niet recht onder de eerste zou plaatsen maar bijvoorbeeld
# recht onder de ‘i’ van het if-statement?

score = int(input("wat is je score? "))

if score > 15:
    geslaagd = "met eens score van " + str(score) + " ben je geslaagd"
    print (geslaagd)

else:
    gezakt = "met eens score van " + str(score) + " ben je gezakt"
    print(gezakt)
