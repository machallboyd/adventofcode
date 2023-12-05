from collections.abc import Generator

with open('d2.txt') as f:
    steplines = f.read().splitlines()

grid1 = [
    [None, None, None, None, None],
    [None, '1','2','3', None],
    [None, '4','5','6', None],
    [None, '7','8','9', None],
    [None, None, None, None, None]
]

grid2 = [
    [None, None, None, None, None, None, None],
    [None, None, None, '1', None, None, None],
    [None, None, '2', '3', '4', None, None ],
    [None, '5', '6', '7', '8', '9', None],
    [None, None, 'A', 'B', 'C', None, None ],
    [None, None, None, 'D', None, None, None],
    [None, None, None, None, None, None, None]
]

ords = {
    'R': [0, 1],
    'L': [0, -1],
    'U': [-1, 0],
    'D': [1, 0]
}

def start_coords(grid: list[str]) -> list[int]:
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == '5':
                return [i, j]
def process(lines: list[str], grid) -> Generator[list[int]]:
    curr = start_coords(grid)
    for line in lines:
        for character in line:
            step = ords[character]
            new = [curr[0] + step[0], curr[1] + step[1]]
            if grid[new[0]][new[1]]:
                curr = new
        yield grid[curr[0]][curr[1]]

print(list(process(steplines, grid1)))
print(list(process(steplines, grid2)))
