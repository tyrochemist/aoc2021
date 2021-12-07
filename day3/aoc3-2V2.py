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

def least_common(entry_list, position):
    zeroes_count = 0
    ones_count = 0
    for entry in entry_list:
        if entry[position] == '0':
            zeroes_count += 1
        else:
            ones_count += 1
    if ones_count > zeroes_count:
        return '0'
    else:
        return '1'

oxygen_rating = diagnostic
for bit in range(len(diagnostic[0])):
    oxygen_current = []
    for entry in oxygen_rating:
        if entry[bit] == most_common(oxygen_rating, bit):
            oxygen_current.append(entry)
    oxygen_rating = oxygen_current
    if len(oxygen_rating) == 1:
        break
co2_rating = diagnostic
for bit in range(len(diagnostic[0])):
    co2_current = []
    for entry in co2_rating:
        if entry[bit] == least_common(co2_rating, bit):
            co2_current.append(entry)
    co2_rating = co2_current
    if len(co2_rating) == 1:
        break
oxygen_rating_decimal = int(oxygen_rating[0], 2)
print(f'Oxygen rating is {oxygen_rating} in binary or {oxygen_rating_decimal} in decimal')
co2_rating_decimal = int(co2_rating[0], 2)
print(f'CO2 rating is {co2_rating} in binary or {co2_rating_decimal} in decimal')
life_support_rating = oxygen_rating_decimal * co2_rating_decimal
print(f'Life support rating is {life_support_rating}')