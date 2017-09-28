# Schrijf een nieuw programma waarin een list met minimaal 10 strings wordt ingelezen. Het programma
# plaatst alle vier-letter strings uit de ingelezen list in een nieuwe list en drukt deze af. Inlezen van een
# lijst kan met eval(input("Geef lijst met minimaal 10 strings: ")).

def vierletters():
    strings = input('Voer 10 strings in: ')
    aparte_woorden = strings.split()

    lijst = []

    for x in aparte_woorden:
        tellen = len(x)
        if tellen < 5:
            lijst.append(x)
    print(lijst)


vierletters()