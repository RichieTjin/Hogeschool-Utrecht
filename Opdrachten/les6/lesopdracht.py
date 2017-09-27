def acronym(phrase):
    'return the acronym of the input string phrase'

    # split phrase into a list of words
    thethinggoes = phrase.split()

    # accumulate first character, as an uppercase, of every word
    res = ''
    for brakrakra in thethinggoes:
        res += brakrakra[0].upper()
    return res

print(acronym('henk peter ria en joke'))


def nested(n):
    for j in range(n):
        for i in range(n):
            print(i, end=' ')
        print()
nested(20)
