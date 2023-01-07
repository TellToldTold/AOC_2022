
def sc(op, me):
    sc = 0
    if me == 'X':
        sc += 1
        if op == 'C':
            sc += 6
        elif op == 'A':
            sc += 3
    elif me == 'Y':
        sc += 2
        if op == 'A':
            sc += 6
        elif op == 'B':
            sc += 3
    else:
        sc += 3
        if op == 'B':
            sc += 6
        elif op == 'C':
            sc += 3
    return sc

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.readlines()
        score = 0

        for line in lines:
            k = line.split(' ')
            score += sc(k[0].strip(), k[1].strip())

        print(score)