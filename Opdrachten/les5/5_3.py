def test(bestandnaam):
    file = open(bestandnaam)
    infile = file.read()
    file.close()
    return infile

kaartnummers = test('kaartnummers.txt').splitlines()
aantal = kaartnummers.count()

for banaan in kaartnummers:
    text = banaan.split(',')
    print(text[1] + ' heeft kaartnummer ' + text[0])


# Deze file telt 6 regels
# Het grootste kaartnummer is: 645345 en dat staat op regel 4