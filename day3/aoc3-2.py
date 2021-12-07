# Read in text and strip newlines
with open('input.txt') as binary_raw:
    binary = binary_raw.readlines()
    diagnostic = [val.rstrip() for val in binary]
most_common = ''
least_common = ''
# Enumerate over bit position, finding most_common
for count in range(len(diagnostic[0])):
    # Set up counters
    ones_count = 0
    zeros_count = 0
    # Iterate over each entry, counting 1s and 0s
    for row in diagnostic:
        if row[count] == '1':
            ones_count += 1
        else:
            zeros_count += 1
    # Determine if there were more 0s or 1s
    if ones_count > zeros_count:
        most_common = '1'
        least_common = '0'
    elif zeros_count > ones_count:
        most_common = '0'
        least_common = '1'
    else:
        most_common = '1'
        least_common = '0'
    print(f'Most common at position {count} is {most_common}')
    print(f'Least common at position {count} is {least_common}')
    # Oxygen generator rating:
    # For each bit, go through and add entry to new list if starts with the most common
    oxygen_ratings = diagnostic
    for bit_count in range(len(diagnostic[0])):
        oxygen_current = []
        for row_count, row in enumerate(oxygen_ratings):
            if row[bit_count] == most_common:
                oxygen_current.append(row)
        if len(oxygen_current) == 1:
            break
        if len(oxygen_current) != 0:
            oxygen_ratings = oxygen_current
    # CO2 generator rating:
    # For each bit, go through and add entry to new list if starts with the least common
    co2_ratings = diagnostic
    for bit_count in range(len(diagnostic[0])):
        co2_current = []
        for row_count, row in enumerate(co2_ratings):
            if row[bit_count] == least_common:
                co2_current.append(row)
        if len(co2_current) == 1:
            break
        if len(co2_current) != 0:
            co2_ratings = co2_current
oxygen_rating = int(oxygen_current[0], 2)
print(f'Oxygen rating is {oxygen_current} in binary or {oxygen_rating} in decimal')
co2_rating = int(co2_current[0], 2)
print(f'CO2 rating is {co2_current} in binary or {co2_rating} in decimal')
life_support_rating = oxygen_rating * co2_rating
print(f'Life support rating is {life_support_rating}')
