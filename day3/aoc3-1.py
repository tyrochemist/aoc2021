with open('input.txt') as binaryRaw:
    binary = binaryRaw.readlines()
    binary_stripped = [val.rstrip() for val in binary]
# Create list to fill with sums of columns
cumulative = []
gamma_digits = []
epsilon_digits = []
# Enumerate over rows of binary text
for row_count, row in enumerate(binary_stripped):
    # Enumerate over each value in the row
    for col_count, column in enumerate(row):
        # For the first row, generate the cumulative list to later be added to
        if row_count == 0:
            cumulative.append(int(column))
        # For every other row, add the current value to the appropriate column, essentially measuring 1s
        else:
            cumulative[col_count] += int(column)
# Check if each value in cumulative is less than or greater than the length minus the value
# This determines if there are more 0s than 1s over course of binary input
for sum1 in cumulative:
    if len(binary)-sum1 > sum1:
        # Append 0 to gamma and 1 to epsilon if there are more values than 1s
        gamma_digits.append(0)
        epsilon_digits.append(1)
    else:
        # Append 1 to gamma and 0 to epsilon if there are more 1s than values
        gamma_digits.append(1)
        epsilon_digits.append(0)
# Convert lists of digits to binary strings
gamma = ''.join(map(str,gamma_digits))
epsilon = ''.join(map(str,epsilon_digits))
# Convert binary strings to decimal
gamma_dec = int(gamma, 2)
epsilon_dec = int(epsilon, 2)
# Obtain power consumption
power_consumption = gamma_dec * epsilon_dec
print(f'Gamma is {gamma} or {gamma_dec} in decimal')
print(f'Epsilon is {epsilon} or {epsilon_dec} in decimal')
print(f'Power consumption is {power_consumption}')
# Gamma is 110000111111 or 3135 in decimal
# Epsilon is 001111000000 or 960 in decimal
# Power consumption is 3009600
