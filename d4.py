from collections import defaultdict
from collections.abc import Generator


class Room:
    def __init__(self, line: str):
        chunks = line.split('-')
        id_checksum = chunks.pop()
        id, checksum = id_checksum.split('[')
        self.id = int(id)
        self.checksum = checksum.split(']')[0]
        self.name = ''.join(chunks)
        self.fullname = '-'.join(chunks)

    def hash(self):
        charcount = defaultdict(int)
        for character in self.name:
            charcount[character] += 1
        count_tuples = [(key, value) for key, value in charcount.items()]
        count_tuples.sort(key=lambda x: (-x[1], x[0]))
        return ''.join(tup[0] for tup in count_tuples[:5])

    def valid(self):
        return self.checksum == self.hash()

    def decode(self):
        def _decode() -> Generator[str]:
            for character in self.fullname:
                match character:
                    case '-':
                        yield ' '
                    case _:
                        yield chr(((ord(character) - 97) + self.id) % 26 + 97)

        return ''.join(_decode())

with open('d4.txt') as f:
    lines = f.read().splitlines()

rooms = [Room(line) for line in lines]
print(sum(room.id for room in rooms if room.valid()))

for room in rooms:
    if room.valid():
        print(room.id)
        print(room.decode())
