
with open('input.txt') as f:
    lines = f.readlines()

    tot = 0
    prev = 10000000
    for i in range(3):
        top = 0
        cur = 0
        for line in lines:
            if line == '\n':
                if cur > top and cur < prev:
                    top = cur
                cur = 0
            else:
                cur += int(line)
        prev = top
        tot += top
    print(tot)
