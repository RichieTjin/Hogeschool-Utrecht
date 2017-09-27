# Schrijf een functie convert() waar je een temperatuur in graden Celsius (als parameter van deze
# functie) kunt omzetten naar graden Fahrenheit. Je kunt de temperatuur in Fahrenheit berekenen met
# de formule T(°F) = T(°C) × 1.8 + 32. Dus 25 °C = 25 * 1.8 + 32 = 77 °F.

def convert(celsius):
    celsius = (celsius * 1.8) + 32
    return float(celsius)


# Schrijf nu ook een tweede functie table() waarin je met een for-loop van -30 °C t/m 40 °C in stappen
# van 10 graden de temperatuur in Fahrenheit print. Zorg middels een geformatteerde output voor
# dezelfde precisie en uitlijning als het voorbeeld hieronder:
# Uitvoer:
#  F C
# -22.0 -30.0
# -4.0 -20.0
# 14.0 -10.0
# 32.0 0.0
# 50.0 10.0
# 68.0 20.0
# 86.0 30.0
# 104.0 40.0

def table():
    for celsius in range(-30, 41, 10):
        print('{:5.1f} {:5.1f}'.format(convert(celsius), celsius))

table()

