# Read in text and strip newlines
with open('input.txt') as binary_raw:
    binary = binary_raw.readlines()
    diagnostic = [val.rstrip() for val in binary]


# Make function that finds most common bit at position
def most_common(entry_list, position):
    zeroes_count = 0
    ones_count = 0
    for entry in entry_list:
        if entry[position] == '0':
            zeroes_count += 1
        else:
            ones_count += 1
    if zeroes_count > ones_count:
        return '0'
    else:
        return '1'


# Make function that finds least common bit at position
def least_common(entry_list, position):
    zeroes_count = 0
    ones_count = 0
    for entry in entry_list:
        if entry[position] == '0':
            zeroes_count += 1
        else:
            ones_count += 1
    if zeroes_count > ones_count:
        return '1'
    else:
        return '0'


oxygen_rating = diagnostic
# Loops through bit positions
for bit in range(len(diagnostic[0])):
    oxygen_current = []
    # Loops through entries at given bit position
    for entry in oxygen_rating:
        # Calculates most_common and then compares to current bit in current entry, adds it if it matches
        if entry[bit] == most_common(oxygen_rating, bit):
            oxygen_current.append(entry)
    oxygen_rating = oxygen_current
    # If the list only has 1 entry remaining, break
    if len(oxygen_rating) == 1:
        break
co2_rating = diagnostic
# Loops through bit positions
for bit in range(len(diagnostic[0])):
    co2_current = []
    # Loops through entries at given bit position
    for entry in co2_rating:
        # Calculates least_common and then compares to current bit in current entry, adds it if it matches
        if entry[bit] == least_common(co2_rating, bit):
            co2_current.append(entry)
    co2_rating = co2_current
    # If the list only has 1 entry remaining, break
    if len(co2_rating) == 1:
        break
# Converts remaining oxygen rating to decimal
oxygen_rating_decimal = int(oxygen_rating[0], 2)
print(f'Oxygen rating is {oxygen_rating[0]} in binary or {oxygen_rating_decimal} in decimal')
# Converts remaining CO2 rating to decimal
co2_rating_decimal = int(co2_rating[0], 2)
print(f'CO2 rating is {co2_rating[0]} in binary or {co2_rating_decimal} in decimal')
# Multiples ratings together
life_support_rating = oxygen_rating_decimal * co2_rating_decimal
print(f'Life support rating is {life_support_rating}')

# Oxygen rating is 111101100011 in binary or 3939 in decimal
# CO2 rating is 011011100010 in binary or 1762 in decimal
# Life support rating is 6940518
