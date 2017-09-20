# 1_1
# vraag: noteer van elke expressie wat de uitkomst en type is:

#invoer             Uitkomst        Type
# 5                 5               Integer
# 5.0               5.0             Floating point
# 5 % 2             1               Integer
# ‘5’               '5'             String
# 5 * 2             10              Integer
# ‘5’ * 2           '55'            String
# ‘5’ + ‘2’         '52'            String
# 5 / 2             2.5             Integer
# 5//2              2               Integer
# [5, 2, 1]         [5,2,1]         List
# 5 in [1, 4, 6]    false           Boolean




# 1_2
# Schrijf en evalueer Python expressies die de volgende vragen beantwoorden:

# a. Hoeveel letters zijn er in 'Supercalifragilisticexpialidocious'?
len('Supercalifragilisticexpialidocious')
34

# b. Komt in 'Supercalifragilisticexpialidocious' de tekst 'ice' voor?
a = 'Supercalifragilisticexpialidocious'
a.count('ice')
1

# c. Is het woord 'Antidisestablishmentarianism' langer dan 'Honorificabilitudinitatibus'?
len('Antidisestablishmentarianism') > len('Honorificabilitudinitatibus')
True

# d. Welke componist komt in alfabetische volgorde het eerst: 'Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein'? Welke het laatst?
list = ['Bartok', 'Bellini', 'Berlioz', 'Bernstein', 'Borodin', 'Brian', 'Buxtehude']
sorted(list)
['Bartok', 'Bellini', 'Berlioz', 'Bernstein', 'Borodin', 'Brian', 'Buxtehude']
'Bartok komt het eerst en Buxtehude het laatst.'




# 1_3
# Schrijf Python statements die het volgende doen:

# 1. Ken de waarde 6 toe aan variabele a, en waarde 7 aan variabele b.
a = 6
b = 7

# 2. Ken aan variabele c als waarde het gemiddelde van a en b toe.
c = (a + b) / 2
6.5

# 3. Ken aan variabele inventaris de een lijst van strings toe: ‘papier’, ‘nietjes’, en ‘pennen’.
inventaris = ['papier', 'nietjes', 'pennen']

# 4. Ken aan variabelen voornaam, tussenvoegsel en achternaam je eigen naamgegevens toe.
voornaam = 'richie'
tussenvoegsel = ''
achternaam = 'tjin'

# 5. Ken aan variabele mijnnaam de variabelen van opdracht 4 (met spaties er tussen) toe.
mijnnaam = voornaam + ' ' + tussenvoegsel + achternaam
mijnnaam
'richie tjin'




# 1_4
# Schrijf booleaanse expressies die van de variabelen van Practice Exercise 1_3 evalueren of:

# 1. 6.75 groter is dan a en kleiner b.
6.75 > a and 6.75 < b
True


# 2. de lengte van inventaris meer dan 5 keer zo groot is als de lengte van variabele mijnnaam.
len(inventaris) > len(mijnnaam)
False

# 3. de lijst inventaris leeg is, of juist meer dan 10 items bevat.
len(inventaris) == 0 or len(inventaris) > 10
False




# 1_5
# We gaan een lijst bijhouden met je favoriete artiesten. We gaan de lijst eerst creëren met 1 artiest en
# dan uitbreiden. Schrijf per stap een expressie om:

# 1. een nieuwe list met 1 artiest aan te maken met de naam favorieten.
list = ['chris brown']

# 2. de lijst uit te breiden met een tweede artiest.
list = list + ['akon']

# 3. de tweede artiest te vervangen door een andere naam.
list[1] = ['pieter']



# 1_6
# Het bereik van een lijst is het verschil tussen het grootste en het kleinste getal. Schrijf een Python
# expressie die het bereik van een lijst berekent. Als bijvoorbeeld variabele list bestaat uit de getallen 3,
# 7, -2 en 12, dan moet de expressie evalueren naar 14 (verschil tussen 12 en -2). Zorg dat de expressie
# altijd werkt, ook al bestaat de lijst uit andere waarden!

abs(a - b)