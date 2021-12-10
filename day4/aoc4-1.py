with open('input.txt') as input_raw:
    input_unstripped = input_raw.readlines()
input_temp = [val.rstrip() for val in input_unstripped]
input_final = [i for i in input_temp if i]
sequence = input_final[0]
print(sequence)
boards = input_final
del boards[0]
print(boards)
for board in boards:
    # Check rows