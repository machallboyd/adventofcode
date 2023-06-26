from collections import defaultdict

inputs = 'L1, R3, R1, L5, L2, L5, R4, L2, R2, R2, L2, R1, L5, R3, L4, L1, L2, R3, R5, L2, R5, L1, R2, L5, R4, R2, R2, L1, L1, R1, L3, L1, R1, L3, R5, R3, R3, L4, R4, L2, L4, R1, R1, L193, R2, L1, R54, R1, L1, R71, L4, R3, R191, R3, R2, L4, R3, R2, L2, L4, L5, R4, R1, L2, L2, L3, L2, L1, R4, R1, R5, R3, L5, R3, R4, L2, R3, L1, L3, L3, L5, L1, L3, L3, L1, R3, L3, L2, R1, L3, L1, R5, R4, R3, R2, R3, L1, L2, R4, L3, R1, L1, L1, R5, R2, R4, R5, L1, L1, R1, L2, L4, R3, L1, L3, R5, R4, R3, R3, L2, R2, L1, R4, R2, L3, L4, L2, R2, R2, L4, R3, R5, L2, R2, R4, R5, L2, L3, L2, R5, L4, L2, R3, L5, R2, L1, R1, R3, R3, L5, L2, L2, R5'
# inputs = 'R8, R4, R4, R8'

ords = {
    'e': [0, 1],
    'w': [0, -1],
    'n': [1, 0],
    's': [-1, 0]
}

rotations = {
        'n': {'L': 'w', 'R': 'e'},
        'e': {'L': 'n', 'R': 's'},
        's': {'L': 'e', 'R': 'w'},
        'w': {'L': 's', 'R': 'n'},
    }

class Navigator:

    def __init__(self, instructions, stop_on_revisit = False):
        self.instructions = instructions.split(', ')
        self.currdir = 'n'
        self.visted = set()
        self.stop_on_revisit = stop_on_revisit
        self.location = [0, 0]
        self.visted.add(tuple(self.location))

    def walk(self, lr: str, dist: int):
        self.currdir = rotations[self.currdir][lr]
        movement = ords[self.currdir]
        steps = dist
        while steps > 0:
            self.location = [self.location[0] + movement[0], self.location[1] + movement[1]]
            if self.stop_on_revisit and tuple(self.location) in self.visted:
                self.report()
            self.visted.add(tuple(self.location))
            steps -= 1

    def journey(self):
        for instruction in self.instructions:
            dist = instruction[1:]
            self.walk(instruction[0], int(dist))

    def report(self):
        print(f'current location is {self.location}')
        print(f'City block distance is {abs(self.location[0]) + abs(self.location[1])}')



navigator = Navigator(inputs)
navigator.journey()
navigator.report()

navigator2 = Navigator(inputs, True)
navigator2.journey()




