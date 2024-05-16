from random import randrange


def create_board(size):
    row = []
    square = []
    numbers = "  "
    for i in range(size):
        row = []
        for a in range(size):
            row.append("?")
        square.append(row)
        del row
        numbers += str(i + 1) + ' ' * 4
        if len(str(i + 2)) >= 2:
            numbers = numbers[:-1]
    return square, numbers


def draw_board_on_screen(square, numbers, alphabet):
    print(' ' * 2 + str(numbers))
    for e in range(len(square)):
        print(alphabet[e] + ' ' + str(square[e]))
        e += 1


def game(square, numbers, alphabet, ship_location):
    draw_board_on_screen(square, numbers, alphabet)
    print("Demande de tir")
    coordinates = input("Quelle coordonée ? ")
    shot_column = int(coordinates[1]) - 1
    shot_row = int(alphabet.index(coordinates[0]))

    if [shot_column, shot_row] != ship_location:
        print("Raté")
        square[shot_row][shot_column] = "~"
        return True
    else:
        print("Bien joué !")
        square[shot_row][shot_column] = "X"
        draw_board_on_screen(square, numbers, alphabet)
        return False


def main():
    keep = True
    size = int(input("Board game size ? "))
    size = 17 if size > 17 else size
    ship_location = [randrange(0, size), randrange(0, size)]
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q"]
    square, numbers = create_board(size)
    while keep:
        keep = game(square, numbers, alphabet, ship_location)


main()
