# Schrijf een programma met twee for-loops in elkaar (nested) om de tafels van 1 t/m 10 uit te printen.

for n in range(1, 11):
    for i in range(1, 11):
        print(n, 'x', i, '=', (n*i))