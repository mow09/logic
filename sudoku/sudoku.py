"""Sudoku AI."""
from display_sudoku import display_sudoku, sudoku_71


class Area:
    """One area of 81 areas in a sudoku."""

    def __init__(self, n, m, v, exist):
        """Initiale position, value."""
        self.n = n
        self.m = m
        self.v = v
        self.possibility = []
        self.exist = exist
        # self.existing = []


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
        self.superareas = [[], [], [], [], [], [], [], [], []]
        self.missing_areas = []
        self.counts = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        # self.superarea =

    def display(self):
        """Display the horizontal lines in sudoku style."""
        for j, h in enumerate(self.horizontals):
            line = ''
            for i, value in enumerate(h):
                if not isinstance(value, int):
                    value = value.v
                line += ' ' + str(value)
                if i in [2, 5]:
                    line += ' |'

            print(line)
            if j in [2, 5]:
                print('-------+-------+------')
        print()

    def fill_superarea(self, n, m, val):
        """Get a list of values in SuperAreas."""
        if n < 3 and m < 3:
            self.superareas[0].append(val)
        if n < 3 and m > 2 and m < 6:
            self.superareas[1].append(val)
        if n < 3 and m > 5:
            self.superareas[2].append(val)
        if n > 2 and n < 6 and m < 3:
            self.superareas[3].append(val)
        if n > 2 and n < 6 and m > 2 and m < 6:
            self.superareas[4].append(val)
        if n > 2 and n < 6 and m > 5:
            self.superareas[5].append(val)
        if n > 5 and m < 3:
            self.superareas[6].append(val)
        if n > 5 and m > 2 and m < 6:
            self.superareas[7].append(val)
        if n > 5 and m > 5:
            self.superareas[8].append(val)
        # self.superareas[1-9].append(val)

    def fill_values(self, horizontals):
        """Fill the sudoku with existing values and ZEROS."""
        for n, h in enumerate(horizontals):
            # run through m
            for m, val in enumerate(h.split()):
                value = int(val)
                if value != 0:
                    existing = True
                    self.counts[value-1] += 1
                else:
                    existing = False
                    self.missing_areas.append((n, m))
                # print(self.counts)
                self.horizontals[n].append(Area(n, m, value, existing))
                self.verticals[m].append(Area(n, m, value, existing))
                self.fill_superarea(n, m, value)

    def get_order(self):
        """Return a list sorted by amount."""
        holder = self.counts.copy()
        order = list()
        counter = 0
        while sum(holder) > 0:
            max_value = max(holder)
            max_index = holder.index(max_value)
            holder[max_index] = 0
            if counter > 20:
                break
            counter += 1
            order.append(max_index+1)
        return order

    def get_horizontals(self):
        """Get the horizontal list of lists."""
        return self.horizontals

    def get_verticals(self):
        """Get the vertical list of lists."""
        return self.verticals

    def run_order(self):
        """Runs through each SuperArea"""
        for number in self.get_order():
            print('searched:', number)
            for each in range(9):
                print('Area number:', each)
                if number not in self.superareas[each]:
                    print('SuperArea', each, 'has no number', number)
                    print()
                    # print('SuperArea', area, 'has no number: ', number)
                break
            break


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

    s.fill_values(h_test)

    for n, (h, vert) in enumerate(zip(s.horizontals, s.verticals)):
        for m, (a, b) in enumerate(zip(h, vert)):
            # print('test:', n, m, a.v)
            assert a.v == int(h_test[n].split()[m])
            assert b.v == int(h_test[m].split()[n])

    # display_sudoku(sudoku_71())
    # # display(s.get_horizontals())
    # s.display()
    # print(s.superareas)
    # print('\n')
    s.run_order()
    # print(s.missing_areas)
    # print(s.counts)
    # print('Order:', s.get_order())


if __name__ == "__main__":
    main()
