inputs = 'L1, R3, R1, L5, L2, L5, R4, L2, R2, R2, L2, R1, L5, R3, L4, L1, L2, R3, R5, L2, R5, L1, R2, L5, R4, R2, R2, L1, L1, R1, L3, L1, R1, L3, R5, R3, R3, L4, R4, L2, L4, R1, R1, L193, R2, L1, R54, R1, L1, R71, L4, R3, R191, R3, R2, L4, R3, R2, L2, L4, L5, R4, R1, L2, L2, L3, L2, L1, R4, R1, R5, R3, L5, R3, R4, L2, R3, L1, L3, L3, L5, L1, L3, L3, L1, R3, L3, L2, R1, L3, L1, R5, R4, R3, R2, R3, L1, L2, R4, L3, R1, L1, L1, R5, R2, R4, R5, L1, L1, R1, L2, L4, R3, L1, L3, R5, R4, R3, R3, L2, R2, L1, R4, R2, L3, L4, L2, R2, R2, L4, R3, R5, L2, R2, R4, R5, L2, L3, L2, R5, L4, L2, R3, L5, R2, L1, R1, R3, R3, L5, L2, L2, R5'

steps = inputs.split(', ')

class Direction:
    map = {
        'n': {'L': 'w', 'R': 'e'},
        'e': {'L': 'n', 'R': 's'},
        's': {'L': 'e', 'R': 'w'},
        'w': {'L': 's', 'R': 'n'},
    }

    def __init__(self):
        self.totals = {
            'n': 0,
            'e': 0,
            's': 0,
            'w': 0,
        }
        self.currdir = 'n'

    def step(self, lr, dist):
        self.currdir = self.map[self.currdir][lr]
        self.totals[self.currdir] += dist

    def report(self):
        vert = abs(self.totals['n'] - self.totals['s'])
        horz = abs(self.totals['e'] - self.totals['w'])
        print(f'total distance is {vert + horz}')

directions = Direction()
for step in steps:
    dist = step[1:]
    directions.step(step[0], int(dist))
directions.report()


