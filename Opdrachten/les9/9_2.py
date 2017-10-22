import time
file = 'inloggers.csv'

tijd = time.strftime('%a %d %b %Y at %H:%M')
while True:
    naam = input("Wat is je achternaam? ")
    voorl = input("Wat zijn je voorletters? ")
    gbdatum = input("Wat is je geboortedatum? ")
    email = input("Wat is je e-mail adres? ")
    with open(file, "a") as bestand:
        bestand.write(tijd + ';' + voorl + ';' + naam + ';' + gbdatum + ';' + email + "\n")
        bestand.close()
    break
