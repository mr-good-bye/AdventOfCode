def calculate_fuel(mass):
    res = 0
    while mass > 8:
        mass = mass//3-2
        res += mass
    return res



inp = ''
masses = list()
while inp != 'exit':
    inp = input()
    if inp.isdecimal():
        masses.append(int(inp))
result = 0
for i in masses:
    result += calculate_fuel(i)
print(result)
