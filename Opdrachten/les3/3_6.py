# Schrijf een for-loop die langs alle letters van een string loopt en de letter uitprint, maar alleen als het
# een klinker is ('aeiou'). Gebruik string s = "Guido van Rossum heeft programmeertaal
# Python bedacht."

zin = 'Guido van Rossum heeft programmeertaal Python bedacht.'

for letter in zin:
    if letter in ['a', 'e', 'i', 'o', 'u']:
        print(letter)