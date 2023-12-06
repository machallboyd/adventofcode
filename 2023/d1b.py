from pathlib import Path
from collections.abc import Generator, Iterable

p = Path(__file__).with_name('d1.txt')

word2number = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}
def converter(calibration: str) -> Generator[int]:
    for i in range(len(calibration)):
        for test_len in range(1, 6):
            if valid := word2number.get(calibration[i: i+test_len]):
                yield valid

def firstlast(digitized: Iterable[list[int]]) -> Generator[int]:
    for digits in digitized:
        yield int(str(digits[0])+str(digits[-1]))

lines = p.open('r').readlines()
print(sum(firstlast(list(converter(line)) for line in lines)))
