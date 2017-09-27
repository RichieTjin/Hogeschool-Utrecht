def test(bestandnaam):
    file = open(bestandnaam)
    infile = file.read()
    file.close()
    return infile

kaartnummers = test('kaartnummers.txt').splitlines()

print('Deze file heeft ' + str(len(kaartnummers)) + ' regels')

print('Het grootste kaartnummer is: ' + str(max(kaartnummers)) + 'en dat staat op regel ')

# for banaan in kaartnummers:
#     text = banaan.split()
#
#     print(text[1] + ' heeft kaartnummer ' + text[0])