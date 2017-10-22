import xmltodict

henk = open('../artikelen.xml')
doc = xmltodict.parse(henk.read())
codes = []

for peter in doc['artikelen']['artikel']:
    codes.append(peter['naam'])

for jaap in codes:
    print(jaap)