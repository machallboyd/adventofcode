ON = '#'
OFF = '.'

class Screen:
    def __init__(self, x: int, y: int):
        self.screen = [[OFF for _ in range(x)] for _ in range(y)]

    def rect(self, x: int, y: int):
        for h in range(y):
            for v in range(x):
                self.screen[h][v] = ON

    def display(self):
        for row in self.screen:
            for chara in row:
                print(chara, end='')
            print('\n', end='')

    def rotate_column(self, x: int, by: int):
        oldcol = [row[x] for row in self.screen]
        newcol = [oldcol[i - by % len(oldcol)] for i in range(len(oldcol))]
        for i, chara in enumerate(newcol):
            self.screen[i][x] = chara
    def rotate_row(self, y: int, by: int):
        oldrow = [chara for chara in self.screen[y]]
        newrow = [oldrow[i - by % len(oldrow)] for i in range(len(oldrow))]
        self.screen[y] = newrow

    def parse(self, command: str):
        tokens = command.split()
        match tokens:
            case ['rect', coords]:
                x, y = coords.split('x')
                self.rect(int(x), int(y))
            case ['rotate', 'column', x_str, 'by', by]:
                x = int(x_str.split('x=')[1])
                self.rotate_column(x, int(by))
            case ['rotate', 'row', y_str, 'by', by]:
                y = int(y_str.split('y=')[1])
                self.rotate_row(y, int(by))
            case _:
                raise ValueError

    def voltage(self):
        print(sum(1 for row in self.screen for chara in row if chara == ON))

screen = Screen(50, 6)
with open('d8.txt') as f:
    commands = f.read().splitlines()
for command in commands:
    screen.parse(command)

screen.display()
screen.voltage()
