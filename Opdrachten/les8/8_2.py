list = 0

def monopolyworp():
    import random

    global list

    while True:
        dobbelsteen_1 = random.randrange(1, 7)
        dobbelsteen_2 = random.randrange(1, 7)

        worp_getal = dobbelsteen_1 + dobbelsteen_2

        uitkomst = print(str(dobbelsteen_1) + ' + ' + str(dobbelsteen_2) + ' = ' + str(worp_getal))

        if dobbelsteen_1 == dobbelsteen_2:
            if list == 3:
                print('Direct naar gevangenis')
                list.clear()
                break
            else:
                print('dubbel')
                list += 1
                continue
        else:
            continue
monopolyworp()