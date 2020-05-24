program = list(map(int, input().split(',')))
i = 0
program[1] = 12
program[2] = 2
while program[i] != 99:
    if program[i] == 1:
        program[program[i+3]] = program[program[i+1]] + program[program[i+2]]
    elif program[i] == 2:
        program[program[i+3]] = program[program[i+1]] * program[program[i+2]]
    else:
        print('Error, num is ' + program[i])
    i = i + 4


print(program)
