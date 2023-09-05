infile = 'd9test.txt'
with open(infile, 'r') as f:
    compressed = f.read()

# class CompressionNode:
#     def __init__(self, raw: str, reps: int):
#         self.raw = raw
#         self.length = 0
#         self.reps = None
#         self.payload = []
#
#     def consume(self):
#         for c in self.raw:
#             if c != '(':
#                 self.length += 1
#             else:
#                 local_chars = None
#                 local_reps = None
#                 while (c := next(self.raw)) != ')':

raw_length = len(compressed)

class Source:
    def __init__(self, whole: str):
        self.whole = whole
        self.index = 0
        self.length = len(whole)

    def advance(self, pos=1):
        self.index += 1

    def c(self):
        return self.whole[self.index]

# advance through string
# if not a multiplier instruction, add one to count
# if a multiplier instruction, create an instruction set, launch one recursion per rep at the location of the end of the instruction set, then move the index just past it:
# Maybe we should feed it a start and end rather than move an index? The index itself should be local.
# Add all returns to the count.

#
# def consume(index: int, length=raw_length, multiplier=1):
#     expanded_count = 0
#     while index < length:
#         raw_c = compressed[index]
#         print(raw_c)
#         if raw_c != '(':
#             expanded_count += 1
#             index += 1
#         else:
#             buf_len = ''
#             reps = ''
#             index += 1
#             raw_c = compressed[index]
#             while raw_c != ')':
#                 if raw_c == 'x':
#                     buf_len = int(buf_len)
#                 elif not isinstance(buf_len, int):
#                     buf_len += raw_c
#                 else:
#                     reps += raw_c
#                 index += 1
#                 raw_c = compressed[index]
#                 print(raw_c)
#             index += 1
#             raw_c = compressed[index]
#             print(raw_c)
#             expanded_count += consume(index, int(reps))
#
#     return expanded_count * multiplier
#
# print(consume(0))