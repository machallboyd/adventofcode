from collections.abc import Generator

with open('d3.txt') as f:
    lines = f.read().splitlines()

triangles = [[int(textside) for textside in line.split()] for line in lines]

def valid_by_sum(sides: list[int]) -> bool:
    for i, target in enumerate(sides):
        if not sum(sides[(i + 1):] + sides[:i]) > target:
            return False
    return True

def filter_invalid(triangles: list[list[int]]) -> Generator[list[int]]:
    for triangle in triangles:
        if valid_by_sum(triangle):
            yield triangle

print(len(list(filter_invalid(triangles))))


