# De tuple letters kan in willekeurige volgorde de letters A, B en C bevatten. Bijvoorbeeld:
# letters = ('A', 'C', 'B', 'B', 'C', 'A', 'C', 'C', 'B')
# Maak een nieuw bestand, bijvoorbeeld pe2_1.py, en schrijf een programma dat een nieuwe lijst maakt
# (en print) met het aantal voorkomens van de letters in alfabetische volgorde. Tuple letters bevat 2
# keer ‘A’, 3 keer ‘B’ en 4 keer ‘C’. De lijst die dit programma maakt (en print) is dan: [2, 3, 4].

letters = ('A', 'C', 'B', 'B', 'C', 'A', 'C', 'C', 'B')
lijst = []
lijst.append(letters.count('A'))
lijst.append(letters.count('B'))
lijst.append(letters.count('C'))
print(str(lijst))
