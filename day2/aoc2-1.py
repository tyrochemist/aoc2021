# Import instructions as strings
with open('input.txt') as instructions:
    instructionsList = instructions.readlines()
x = 0
y = 0
product = 0
# Iterate through instructions
for instruction in instructionsList:
    # Split string into command and value
    command = instruction.split()[0]
    units = instruction.split()[1]
    # Check what command is and increment by value
    if command == 'forward':
        x += int(units)
    if command == 'down':
        y += int(units)
    if command == 'up':
        y -= int(units)
# Multiply horizontal distance by depth
product = x*y
print(f'Your horizontal distance is {x} and your depth is {y}')
print(f'The product of the two is {product}')
# Your horizontal distance is 2063 and your depth is 1005
# The product of the two is 2073315