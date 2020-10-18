print('a, b, c, y1, y2')
for i in range(0, 1<<3):
    a, b, c = (i & 4) >> 2, (i & 2) >> 1, i & 1
    y1 = (a & b & c) | (a | b | c) & (~((a & b) | (a & c) | (b & c)))
    y2 = ((a & b) | (a & c) | (b & c))
    print(a, b, c, y1, y2)