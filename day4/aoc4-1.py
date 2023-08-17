with open('input.txt') as input_raw:
    input_unstripped = input_raw.readlines()
input_temp = [val.rstrip() for val in input_unstripped]
print(input_unstripped)
input_final = [i for i in input_temp if i]
sequence = input_final[0]
board_rows = input_final
del board_rows[0]

# def bingosearch(board, sequence):
#     # Check by row
#     row_bingo = None
#     column_bingo = None
#     for row in board:
#         for element in row:
#             if element not in sequence:
#                 break
#         else:
#             row_bingo = True
#             break
#     # Check by column
#     for column in range(len(board[0])):
#         for row in board:
#             if row[column] not in sequence:
#                 break
#         else:
#             column_bingo = True
#             break
#     if row_bingo or column_bingo:
#         return True
#
# answers = []
# for number in sequence:
#     answers.append(number)
#     for board in boards:
#         if bingosearch(board, answers):
#             print("Oooooh! That's a Bingo!")
#             print(f"Sequence is {answers} and board is {board}")
#             break