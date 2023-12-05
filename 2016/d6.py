from collections import defaultdict
from collections.abc import Generator

with open('d6.txt') as f:
    messages = f.read().splitlines()

counts = [defaultdict(int) for _ in range(len(messages[0]))]

for message in messages:
    for i, character in enumerate(message):
        counts[i][character] += 1

def password(counts) -> Generator[str]:
    for placedict in counts:
        yield max(placedict, key=placedict.get)

def real_password(counts) -> Generator[str]:
    for placedict in counts:
        yield min(placedict, key=placedict.get)

print(''.join(real_password(counts)))