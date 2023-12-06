from pathlib import Path
from collections.abc import Generator, Iterable

p = Path(__file__).with_name('d1.txt')

def single_digit(calibration:Iterable[str]) -> int:
    for c in calibration:
        try:
            digit = int(c)
            return digit
        except (ValueError):
            pass

def by_digit(calibration: str):
    first = single_digit(calibration)
    last = single_digit(reversed(calibration))
    return int(str(first) + str(last))

def digital_values(calibrations: Iterable) -> Generator[int]:
    for calibration in calibrations:
        yield by_digit(calibration=calibration)

lines = p.open('r').readlines()
print("by digits:")
print(sum(digital_values(lines)))
