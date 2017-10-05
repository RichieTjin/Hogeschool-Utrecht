# Schrijf een while-loop die steeds getallen van de gebruiker vraagt tot deze 0 ingeeft:

def sum():
    total = 0
    while True:
        number = int(input('geef nummer: '))
        if number == 0:
            break
        total += int(number)
    print(total)

sum()
