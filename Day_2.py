pr = list(map(int, input().split(',')))
def calculate(n, v, program):
    i = 0
    program[1] = n
    program[2] = v
    while program[i] != 99:
        if program[i] == 1:
            program[program[i+3]] = program[program[i+1]] + program[program[i+2]]
        elif program[i] == 2:
            program[program[i+3]] = program[program[i+1]] * program[program[i+2]]
        else:
            return [0,0,0]
        i = i + 4
    return [program[0], n, v]


def trying():
    for n in range(181):
        for v in range(181):
            res = calculate(n, v, pr.copy())
            if res[0] == 19690720:
                print(res)
                return 100*res[1]+res[2]


print(trying())
