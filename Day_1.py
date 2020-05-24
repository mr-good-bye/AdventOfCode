def calculate_fuel(mass):
    return mass//3-2


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
