def next_num(primer):
    number = primer
    while True:
        number += 1
        yield number

def solve_kap(num):
    sqrdnum = str(num ** 2)
    for i in range(1, len(sqrdnum)):
        first, second = int(sqrdnum[:i]), int(sqrdnum[i:])
        if (first + second) == num:
            print(num, sqrdnum, "(%s, %s)" % (first, second))

for x in next_num(1):
    solve_kap(x)
