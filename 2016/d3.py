from collections.abc import Generator, Iterator
from itertools import islice, chain


def batched(iterable, n):
    it = iter(iterable)
    while batch := tuple(islice(it, n)):
        yield batch

def valid_by_sum(sides: list[int]) -> bool:
    for i, target in enumerate(sides):
        if not sum(sides[(i + 1):] + sides[:i]) > target:
            return False
    return True

def filter_invalid(triangles: Iterator[Iterator[int]]) -> Generator[list[int]]:
    for triangle in triangles:
        if valid_by_sum(list(triangle)):
            yield triangle

with open('d3.txt') as f:
    lines = f.read().splitlines()

triangles = [[int(textside) for textside in line.split()] for line in lines]
triangles_rotated = reversed(list(zip(*triangles)))
triangles_rechunked = batched(chain.from_iterable(triangles_rotated), 3)

print(len(triangles))

print(len(list(filter_invalid(triangles_rechunked))))
