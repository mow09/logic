"""Simple visualation for sudoku AI in terminal."""


def sudoku_71():
    """Get result of sudoku 71."""
    h1 = [9, 6, 1, 4, 3, 7, 2, 8, 5]
    h2 = [8, 7, 4, 5, 9, 2, 3, 6, 1]
    h3 = [2, 3, 5, 8, 6, 1, 4, 7, 9]
    h4 = [6, 2, 9, 1, 4, 5, 7, 3, 8]
    h5 = [7, 5, 8, 6, 2, 3, 9, 1, 4]
    h6 = [1, 4, 3, 7, 8, 9, 6, 5, 2]
    h7 = [4, 1, 7, 2, 5, 6, 8, 9, 3]
    h8 = [3, 8, 6, 9, 1, 4, 5, 2, 7]
    h9 = [5, 9, 2, 3, 7, 8, 1, 4, 6]

    return [h1, h2, h3, h4, h5, h6, h7, h8, h9]


def display(horizontal):
    """Display the horizontal lines in sudoku style."""
    for j, h in enumerate(horizontal):
        line = ''
        for i, value in enumerate(h):
            line += ' ' + str(value)
            if (i+1) % 3 == 0 and i != 8:
                line += ' |'

        print(line)
        if (j+1) % 3 == 0 and j != 8:
            print('-------+-------+------')
    print()


def main():
    """Run this in direct call."""
    display(sudoku_71())


if __name__ == "__main__":
    main()
