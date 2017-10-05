print('1: Ik wil weten hoeveel kluizen nog vrij zijn\n','2: Ik wil een nieuwe kluis\n','3: Ik wil even iets uit mijn kluis halen\n','4: Ik geef mijn kluis terug\n')

def keuzemenu():
    number = int(input('Voer het nummer in: '))
    if number == 1:
        toon_aantal_kluizen_vrij()
    elif number == 2:
        nieuwe_kluis()
    elif number == 3:
        kluis_openen()
    elif number == 4:
        kluis_teruggeven()
    else:
        print('verkeerde invoer')
        return

def toon_aantal_kluizen_vrij():
    file = open('kluizen.txt')
    aantal = len(file.readlines())
    file.close()

    aantal_vrije_kluizen = int(12 - aantal)
    if aantal <= aantal_vrije_kluizen:
        print(aantal_vrije_kluizen)
        return
    else:
        print('Er zijn geen kluizen meer beschikbaar!')

def nieuwe_kluis():
    kluis_list = [1,2,3,4,5,6,7,8,9,10,11,12]
    file = open('kluizen.txt')
    lines = file.readlines()
    file.close()

    for x in lines:
        x = x.split(';')
        kluisnummer = int(x[0])
        for kluis in kluis_list:
            if kluis == kluisnummer:
                kluis_list.remove(kluis)
    print(kluis_list)
    return

def kluis_openen():
    print('openen')
    return

def kluis_teruggeven():
    print('teruggeven')
    return

keuzemenu()