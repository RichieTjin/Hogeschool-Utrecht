def monopolyworp():
    import random
    dobbelsteen_1 = random.randrange(1, 7)
    dobbelsteen_2 = random.randrange(1, 7)

    worp_getal = dobbelsteen_1 + dobbelsteen_2

    uitkomst = print(str(dobbelsteen_1) + ' + ' + str(dobbelsteen_2) + ' = ' + str(worp_getal))

    list = 0

    if dobbelsteen_1 == dobbelsteen_2:
        if list == 3:
            print('Direct naar gevangenis')
            list.clear()
            return uitkomst
        else:
            print('dubbel')
            list += 1
            return uitkomst
    else:
        return uitkomst

monopolyworp()