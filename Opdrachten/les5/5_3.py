def test(bestandnaam):
    file = open(bestandnaam)
    infile = file.readlines()
    file.close()
    return infile

kaartnummers = test('kaartnummers.txt')

print('Deze file heeft ' + str(len(kaartnummers)))

hoogstenummer = 0
for huidigeregel in kaartnummers:
    woorden = huidigeregel.split(', ')
    if int(woorden[0]) > hoogstenummer:
        hoogstenummer = int(woorden[0])

print('het hoogste kaartnummer is:', hoogstenummer)


# for banaan in kaartnummers:
#     text = banaan.split()
#
#     print(text[1] + ' heeft kaartnummer ' + text[0])