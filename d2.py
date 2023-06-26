from collections.abc import Generator

with open('d2.txt') as f:
    steplines = f.read().splitlines()

grid = [[1,2,3],[4,5,6],[7,8,9]]

ords = {
    'R': [0, 1],
    'L': [0, -1],
    'U': [-1, 0],
    'D': [1, 0]
}

def process(lines: list[str]) -> Generator[list[int]]:
    curr = [1, 1]
    for line in lines:
        for character in line:
            step = ords[character]
            new = [curr[0] + step[0], curr[1] + step[1]]
            if new[0] in {0, 1, 2} and new[1] in {0, 1, 2}:
                curr = new
        yield grid[curr[0]][curr[1]]

print(list(process(steplines)))
