from pathlib import Path

p = Path(__file__).with_name('d2.txt')

MAXES = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def validate_game(game: str) -> int:
    gametag, draws = game.split(': ')
    _, game_id = gametag.split()
    for draw in draws.split(';'):
        if not possible(draw):
            return 0
    return int(game_id)

def possible(draw: str) -> bool:
    for color_count in draw.split(','):
        count, color = color_count.split()
        if int(count) > MAXES[color]:
            return False
    return True

lines = p.open('r').readlines()
good_games = (validate_game(line) for line in lines)
print(sum(good_games))
