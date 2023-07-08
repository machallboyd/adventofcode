import hashlib
from collections.abc import Generator

puzzle_input = 'ugkcyxxp'

def passgen(input: str, length: int) -> str:
    def _passgen() -> Generator[str]:
        index = 0
        remaining = length
        while remaining > 0:
            seed = input + str(index)
            seedenc = seed.encode('utf-8')
            hash = hashlib.md5(seedenc)
            if (digest := hash.hexdigest())[:5] == '00000':
                yield(digest[5])
                remaining -= 1
            index += 1
    return ''.join(_passgen())

print(passgen(puzzle_input, 8))