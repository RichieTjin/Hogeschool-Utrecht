def test(bestandnaam):
    file = open(bestandnaam)
    infile = file.read()
    file.close()
    return infile

kaartnummers = test('kaartnummers.txt').splitlines()

for banaan in kaartnummers:
    text = banaan.split(',')
    print(text[1] + ' heeft kaartnummer ' + text[0])