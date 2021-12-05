# Read in text and strip newlines
with open('input.txt') as binary_raw:
    binary = binary_raw.readlines()
    diagnostic = [val.rstrip() for val in binary]
    # Make copies to remove elements from
    diagnostic_oxygen = diagnostic
    diagnostic_CO2 = diagnostic
most_common = ''
# Enumerate over bit position
for count, bit in enumerate(diagnostic[0]):
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
        most_common += '1'
    else:
        most_common += '0'
print(most_common)
# Oxygen generator rating: for each bit, go through and remove entry if starts with the least common
for bit_count, bit in enumerate(diagnostic[0]):
    to_remove_oxygen = []
    if len(diagnostic_oxygen) == 1:
        break
    for row_count, row in enumerate(diagnostic_oxygen):
        if row[bit_count] != most_common[bit_count]:
            to_remove_oxygen.append(row_count)
    for i in reversed(to_remove_oxygen):
        del diagnostic_oxygen[i]
# CO2 scrubber rating: for each bit, go through and remove entry if it starts with the most common
for bit_count, bit in enumerate(diagnostic[0]):
    to_remove_co2 = []
    if len(diagnostic_CO2) == 1:
        break
    for row_count, row in enumerate(diagnostic):
        if row[bit_count] == most_common[bit_count]:
            to_remove_co2.append(row_count)
    # If there is only one entry left, stop... this could have a problem if there are "ties"
    for i in reversed(to_remove_co2):
        del diagnostic_CO2[i]
oxygen_rating = int(diagnostic_oxygen[0], 2)
CO2_rating = int(diagnostic_CO2[0], 2)
life_support_rating = oxygen_rating * CO2_rating
print(life_support_rating)
