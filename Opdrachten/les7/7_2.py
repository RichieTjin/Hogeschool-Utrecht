def woord():
    while True:
        woord = input('Geef een woord met 4 letters: ')
        tel_letters = len(woord)
        if tel_letters == 4:
            print('Inlezen van correcte string: ' + woord + ' is geslaagd')
            break
        else:
            print(woord + ' Heeft ' + str(tel_letters) + ' letters')

woord()