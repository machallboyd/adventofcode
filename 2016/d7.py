import re

abba = re.compile(r'(\w)(?!\1)(\w)\2\1')
hypernet_abba = re.compile(r'\[\w*(\w)(?!\1)(\w)\2\1\w*]')

with open('d7.txt') as f:
    addresses = f.read().splitlines()

print('Valid ABBAs:')
valid_abbas = list(address for address in addresses if (abba.search(address) and not hypernet_abba.search(address)))
print(len(valid_abbas))

def splitter(address: str) -> dict[str, list[str]]:

    hypernets = []
    supernets = []
    active = supernets

    for character in address:
        match character:
            case '[':
                active = hypernets
                hypernets.append(' ')
            case ']':
                active = supernets
                supernets.append(' ')
            case _:
                active.append(character)

    return {
        'hypernets': ''.join(hypernets).split(),
        'supernets': ''.join(supernets).split()
    }

aba = re.compile(r'(\w)(?!\1)(\w)\1')
supers = set()

for address in addresses:
    nets = splitter(address)
    for chunk in nets['supernets']:
        for match in aba.finditer(chunk):
            c1, c2 = match.groups()
            bab = f'{c2}{c1}{c2}'
            for schunk in nets['hypernets']:
                if bab in schunk:
                    print(address)
                    print(c1 + c2)
                    supers.add(address)

for address in addresses:
    nets = splitter(address)
    for chunk in nets['hypernets']:
        for match in aba.finditer(chunk):
            c1, c2 = match.groups()
            bab = f'{c2}{c1}{c2}'
            for schunk in nets['supernets']:
                if bab in schunk:
                    print(address)
                    print(c1 + c2)
                    supers.add(address)


print(len(supers))
