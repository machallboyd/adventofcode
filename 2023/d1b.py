from pathlib import Path
from collections.abc import Generator, Iterable

p = Path(__file__).with_name('d1.txt')

word2number = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}
def converter(calibration: str) -> Generator[str]:
    for i in range(len(calibration)):
        if (c := calibration[i]).isdigit():
            yield c
        else:
            for test_len in range(3, 6):
                if valid := word2number.get(calibration[i: i+test_len]):
                    yield valid

def firstlast(digitized: Iterable[list[str]]) -> Generator[int]:
    for digits in digitized:
        yield int(digits[0]+digits[-1])

lines = p.open('r').readlines()
print(sum(firstlast(list(converter(line)) for line in lines)))
