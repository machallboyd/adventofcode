import re

abba = re.compile(r'(\w)(?!\1)(\w)\2\1')
hypernet_abba = re.compile(r'\[\w*(\w)(?!\1)(\w)\2\1\w*]')
aba_then_bab =  re.compile(r'(\w)(?!\1)(\w)\1(?<=\[\w*\2\1\2\w*])')

with open('d7test2.txt') as f:
    addresses = f.read().splitlines()

print('Valid ABBAs:')
valid_abbas = list(address for address in addresses if (abba.search(address) and not hypernet_abba.search(address)))
print(len(valid_abbas))
print('Valid SSLs:')
valid_ssls =
