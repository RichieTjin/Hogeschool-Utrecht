cijfers = {
    'henk': 8.6,
    'peter': 9.9,
    'jan': 6.6,
    'oetnoen': 7.0,
    'willem': 9.5,
    'jantje': 8.4,
    'roadman': 2.9,
    'shaq': 9.2,
    'ties': 5.5,
    }

for key, value in cijfers.items():
    if value > float(9.0):
        print(key, value)