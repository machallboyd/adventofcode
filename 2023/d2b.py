from pathlib import Path
from math import prod

p = Path(__file__).with_name('d2.txt')

def game_power(game: str) -> int:
    _, draws = game.split(': ')
    local_max = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    for draw in draws.split(';'):
        for color_count in draw.split(','):
            count, color = color_count.split()
            if (icount := int(count)) > local_max[color]:
                local_max[color] = icount
    return prod(local_max.values())

lines = p.open('r').readlines()
game_powers = (game_power(line) for line in lines)
print(sum(game_powers))