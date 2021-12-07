# Import instructions as strings
with open('input.txt') as instructions:
    instructionsList = instructions.readlines()
x = 0
y = 0
product = 0
aim = 0
# Iterate through instructions
for instruction in instructionsList:
    # Split string into command and value
    command = instruction.split()[0]
    units = instruction.split()[1]
    # Check what command is and increment by value
    if command == 'forward':
        print(f'Moving forward by {units}')
        y += int(units) * aim
        x += int(units)
    if command == 'down':
        aim += int(units)
    if command == 'up':
        aim -= int(units)
    print(f'Your current depth is {y}, your horizontal position is {x} and your current aim is {aim}')
# Multiply horizontal distance by depth
product = x*y
print(f'Your horizontal distance is {x} and your depth is {y}')
print(f'The product of the two is {product}')
# Your horizontal distance is 2063 and your depth is 892056
# The product of the two is 1840311528