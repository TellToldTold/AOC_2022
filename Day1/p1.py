
with open('input.txt') as f:
    lines = f.readlines()

    top = 0
    cur = 0
    for line in lines:
        if line == '\n':
            top = max(top, cur)
            cur = 0
        else:
            cur += int(line)
    print(top)
