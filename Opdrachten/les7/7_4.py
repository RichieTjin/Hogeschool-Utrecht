def ticker():
    with open('ticker.txt', 'r') as file:
        ticker = {}
        content = file.readlines()
        for line in content:
            line = line.split(':')
            value = line[0].strip()
            key = line[1].strip()
            ticker[key] = value

        choice = int(input('Voer 1 voor tickersymbol of 2 voor bedrijfsnaam: '))
        if choice == 1:
            tick = input('Enter Ticker name ')
            for key, value in ticker.items():
                if key.upper() == tick.upper():
                    return value
        else:
            bedrijf = input('Enter Bedrijfsnaam name ')
            for key, value in ticker.items():
                if value.upper() == bedrijf.upper():
                    return key



print(ticker())