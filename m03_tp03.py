#create tuple of chess board
i = 0
sissa_chess_board = {}
while i < 64:
    sissa_chess_board[i] = 2 ** i
    i += 1

#draw
columns = 8
rows = 8
counter = len(sissa_chess_board)
biggest_number_digits = len(str(sissa_chess_board[counter - 1]))
white_space_to_add = (biggest_number_digits - 1) * " "
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H"]
alphabet_chess_board = []

for i in range(len(alphabet)):
    alphabet_chess_board.append(alphabet[i] + white_space_to_add)

#launch
print("-" * 24 * 8)
for c in range(columns):
    grains = {}
    counter -= 8
    for r in range(rows):
        number_str = str(sissa_chess_board[counter])  #get value for each case
        number_digits = len(number_str)
        white_spaces_to_add = biggest_number_digits - number_digits
        grains[r] = number_str + white_spaces_to_add * " "
        counter += 1
    print("|", list(grains.values()), "|", 8 - c)  #print values after construction of line
    counter -= 8
print("|", list(alphabet_chess_board), "| x")
print("-" * 24 * 8)

def find_number_by_position(position):
    column_number, row_number = split_position_into_numbers(position)
    print("The value for", position, "is :")
    number = sissa_chess_board[(row_number-1)*8+column_number]
    print(number)


def split_position_into_numbers(position):
    letters = []
    for letter in position:
        letters.append(letter)
    return alphabet.index(letters[0]), int(letters[1])


find_number_by_position(input("Welcome to sissa chess board. Tell me a coordinate ? "))


