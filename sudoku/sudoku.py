"""Sudoku AI."""
from display_sudoku import display_sudoku, sudoku_71


class Area:
    """One area of 81 areas in a sudoku."""

    def __init__(self, n, m, v, exist):
        """Initiale position, value."""
        self.n = n
        self.m = m
        self.v = v
        self.pos = n, m
        self.exist = exist
        # self.existing = []

    def is_nr(self):
        return self.v


class SuperArea:
    """One SuperArea contains nice Area."""

    def __init__(self, area):
        self.area = area

    # def is_not_nr(self):
    #     return self.existing


class Sudoku:
    """The class solves the sudoku."""

    def __init__(self, difficulty):
        """Set the difficulty."""
        self.difficulty = difficulty
        self.horizontals = [[], [], [], [], [], [], [], [], []]
        self.verticals = [[], [], [], [], [], [], [], [], []]
        # self.superarea =

    def display(self):
        """Display the horizontal lines in sudoku style."""
        for j, h in enumerate(self.horizontals):
            line = ''
            for i, value in enumerate(h):
                if not isinstance(value, int):
                    value = value.v
                line += ' ' + str(value)
                if (i+1) % 3 == 0 and i != 8:
                    line += ' |'

            print(line)
            if (j+1) % 3 == 0 and j != 8:
                print('-------+-------+------')
        print()

    def missing_areas(self):
        pass

    def get_horizontals(self):
        """Get the horizontal list of lists."""
        return self.horizontals

    def get_verticals(self):
        """Get the vertical list of lists."""
        return self.verticals

    def fill_values(self, horizontals):
        """Fill the sudoku with existing values and ZEROS."""
        for n, h in enumerate(horizontals):
            # run through m
            for m, val in enumerate(h.split()):
                value = int(val)
                if value != 0:
                    existing = True
                else:
                    existing = False
                self.horizontals[n].append(Area(n, m, value, existing))
                self.verticals[m].append(Area(n, m, value, existing))
                # print(a1.n, a1.m, a1.v, a1.exist)
        # self.fill_verticals()
        #
        #     for n, h in enumerate(s.get_horizontals()):
        #         for m, a in enumerate(h):
        #             # print('test:', n, m, a.v)
        #             verti[m].append(a)

# ---


def insert_existing(horizontals):
    # run through n
    for n, h in enumerate(horizontals):
        # run through m
        for m, val in enumerate(h.split()):
            value = int(val)
            if value != 0:
                existing = True
            else:
                existing = False
            a1 = Area(n, m, value, existing)


def main():
    """Run this in direct call."""
    # display(sudoku_71())
    print('main():')

    h1 = '9 6 0 0 0 0 2 0 0'
    h2 = '0 7 0 5 9 2 0 0 0'
    h3 = '0 0 0 8 0 0 0 0 0'
    h4 = '0 2 0 0 0 0 7 0 8'
    h5 = '0 0 8 0 0 0 9 0 0'
    h6 = '1 0 3 0 0 0 0 5 0'
    h7 = '0 0 0 0 0 6 0 0 0'
    h8 = '0 0 0 9 1 4 0 2 0'
    h9 = '0 0 2 0 0 0 0 4 6'

    h_test = [h1, h2, h3, h4, h5, h6, h7, h8, h9]

    s = Sudoku('medium')
    print(s.difficulty)

    # print('horizontals: ', s.get_horizontals())

    s.fill_values(h_test)

    for n, (h, vert) in enumerate(zip(s.get_horizontals(), s.get_verticals())):
        for m, (a, b) in enumerate(zip(h, vert)):
            # print('test:', n, m, a.v)
            assert a.v == int(h_test[n].split()[m])
            assert b.v == int(h_test[m].split()[n])

    # display(s.get_horizontals())
    display_sudoku(sudoku_71())
    s.display()

    # print('veriticals: ', s.get_verticals())

    # insert_existing(h)

    print('\n')


if __name__ == "__main__":
    main()
