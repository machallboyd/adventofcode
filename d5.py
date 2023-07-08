import hashlib
from collections.abc import Generator

puzzle_input = 'ugkcyxxp'

class Password:

    def __init__(self, puzzle_input, length):
        self.puzzle_input = puzzle_input
        self.length = length
        self.password = [None for _ in range(length)]

    def assign(self, position, character):
        try:
            intpos = int(position)
            if self.password[intpos] is None:
                self.password[intpos] = character
        except ValueError:
            return
        except IndexError:
            return

    def report(self):
        print(''.join(self.password))

    def passgen(self) -> str:
        index = 0
        while None in self.password:
            seed = self.puzzle_input + str(index)
            hashed = hashlib.md5(seed.encode('utf-8'))
            if (digest := hashed.hexdigest())[:5] == '00000':
                self.assign(position=digest[5], character=digest[6])
            index += 1

newpass = Password(puzzle_input, 8)
newpass.passgen()
newpass.report()