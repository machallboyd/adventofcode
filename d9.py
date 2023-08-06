
infile = 'd9.txt'

with open(infile, 'r') as f:
    compressed = f.read()


in_multiplier = False
length = ''
multiplier = ''
buffer = ''

out = ''
for character in compressed:
    if in_multiplier:
        if character == 'x':
            length = int(length)
        elif character ==')':
            in_multiplier = False
            multiplier = int(multiplier)
        elif not isinstance(length, int):
            length += character
        else:
            multiplier += character
    elif length: #build the buffer
        buffer += character
        if len(buffer) == length:
            while multiplier > 0:
                multiplier -= 1
                out += buffer
            buffer = ''
            length = ''
            multiplier = ''
    elif character == '(':
        in_multiplier = True
    else:
        out += character

if buffer:
    while multiplier > 0:
        multiplier -= 1
        out += buffer

print(out)
print(len(out.strip()))
