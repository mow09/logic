"""Sudoku AI."""
from display_sudoku import display_sudoku, sudoku_71


class Area:
    """One area of 81 areas in a sudoku."""

    def __init__(self, n, m, v, fix, new=True):
        """Initiale position, value."""
        self.n = n
        self.m = m
        self.v = v
        self.possibility = []
        self.is_fix = fix
        self.is_new = new

    def __str__(self):
        """Show functions."""
        return f"""\n\tcall n: {self.n}, m: {self.m}, v: {self.v}\n\
            is_fix: {self.is_fix}, is_new: {self.is_new}\n\
                possibility: {self.possibility}\n"""

    def __repr__(self):
        """Show results."""
        return f"n: {self.n}, \nm: {self.m}, \nv: {self.v}, \nis_fix: {self.is_fix}, \nis_new: {self.is_new}, \npossibility: {self.possibility}"

    # def __repr__():
    #     """Show it for developer."""
    #
    #
    # def __str__():
    #     """Show it for consumer."""

    # def func(self):


class SuperArea:
    """One SuperArea contains nine Areas."""

    def __init__(self, upper_left, lower_right):
        """Initale the SuperArea."""
        self.upper_left = upper_left
        self.lower_right = lower_right
        self.areas = []
        self.values = []
        # returns how often it is
        self.amount = [0, 0, 0, 0, 0, 0, 0, 0, 0]


class Horizontal:
    """Nine horizontal lines."""

    def __init__(self):
        """Parameter of horizontal line."""
        self.areas = []
        self.values = []

    def make_value_list(self):
        """Make a list of the values."""
        self.values = []
        if len(self.values) == 0:
            for i in range(9):
                self.values.append(self.areas[i].v)


class Vertical:
    """Nine vertical lines."""

    def __init__(self):
        """Parameter of vertical line."""
        self.areas = []
        self.values = []

    def make_value_list(self):
        """Make a list of the values."""
        if len(self.values) != 0:
            self.values = []
        for i in range(9):
            self.values.append(self.areas[i].v)


class Sudoku:
    """The class solves the sudoku."""

    def __init__(self, difficulty):
        """Set the difficulty."""
        self.difficulty = difficulty
        # self.horizontals = [[], [], [], [], [], [], [], [], []]
        # self.verticals = [[], [], [], [], [], [], [], [], []]
        self.horizontals = [Horizontal(),
                            Horizontal(),
                            Horizontal(),
                            Horizontal(),
                            Horizontal(),
                            Horizontal(),
                            Horizontal(),
                            Horizontal(),
                            Horizontal()]
        self.verticals = [Vertical(),
                          Vertical(),
                          Vertical(),
                          Vertical(),
                          Vertical(),
                          Vertical(),
                          Vertical(),
                          Vertical(),
                          Vertical()]
        self.superarea = [SuperArea((0, 0), (2, 2)),
                          SuperArea((0, 3), (2, 5)),
                          SuperArea((0, 6), (2, 8)),
                          SuperArea((3, 0), (5, 2)),
                          SuperArea((3, 3), (5, 5)),
                          SuperArea((3, 6), (5, 8)),
                          SuperArea((6, 0), (8, 2)),
                          SuperArea((6, 3), (8, 5)),
                          SuperArea((6, 6), (8, 8))]
        self.missing_areas = []
        self.counts = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    def display_superarea_amount(self):
        """Display the amount list of all Superareas."""
        print('\nSuperAreaAmount:')
        print('\t      1  2  3  4  5  6  7  8  9')
        for index in range(9):
            line = '['
            for c, i in enumerate(self.superarea[index].amount):
                if i == 0:
                    line += ' '
                else:
                    line += str(i)
                if c < 8:
                    line += ', '
            line += ']'
            print(f'\tSA {index}', line)
            if index in [2, 5]:
                print()

    def display(self):
        """Display the horizontal lines in sudoku style."""
        print()
        print(u'\U00011894', ' is missing')
        print('.V', 'is entered')
        print()
        for j, h in enumerate(self.horizontals):
            line = '\t\t\t'
            for i, area in enumerate(h.areas):
                if not isinstance(area, int):
                    value = area.v
                if value == 0:
                    line += ' ' + u'\U00011894'
                else:
                    if area.is_fix:
                        line += ' ' + str(value)
                    else:
                        line += '.' + str(value)
                if i in [2, 5]:
                    line += ' |'

            print(line)
            if j in [2, 5]:
                print('\t\t\t-------+-------+------')
        print()
        print()

    def display_horizontals(self, spec=10):
        """Display the horizontal lines."""
        if spec == 10:
            for h in self.horizontals:
                line = '\n  '
                for i, area in enumerate(h.areas):
                    if area.v == 0:
                        line += ' ' + u'\U00011894'
                    else:
                        line += ' ' + str(area.v)
                    if i in [2, 5]:
                        line += ' '
                print(line)
                print()
        else:
            h = self.horizontals[spec]
            line = '\n  '
            for i, area in enumerate(h.areas):
                if area.v == 0:
                    line += ' ' + u'\U00011894'
                else:
                    line += ' ' + str(area.v)
                if i in [2, 5]:
                    line += ' '
            print(line)
            print()

    def display_verticals(self, spec=10):
        """Display the vertical lines."""
        if spec == 10:
            for h in self.horizontals:
                line = ''
                for i, area in enumerate(h.areas):
                    if area.v == 0:
                        line += '   ' + u'\U00011894'
                    else:
                        line += '   ' + str(area.v)
                    if i in [2, 5]:
                        line += ' '
                print(line)
        else:
            h = self.verticals[spec]
            line = '\t\t\n'
            for i, area in enumerate(h.areas):
                if area.v == 0:
                    line += u'\t\t\U00011894\n'
                else:
                    line += '\t\t' + str(area.v) + '\n'
                if i in [2, 5]:
                    line += '\n'
            print(line+'\n')

    def display_superarea(self, spec):
        """Display one superarea lines."""
        h = self.superarea[spec]
        line = '\t'
        for i, area in enumerate(h.areas):
            if area.v == 0:
                line += '\t' + u'\U00011894'
            else:
                line += '\t' + str(area.v)
            if i in [2, 5]:
                line += '\n\t'
        print(line)
        # print()

    # def display_area(self, n, m):
    #     """Display direct inpact for area (n,m)."""
    #     for supera in (self.superarea):
    #         # check n
    #         if ((supera.upper_left[0] <= n and n <= supera.lower_right[0]) and
    #                 (supera.upper_left[1] <= m and m <= supera.lower_right[1])):
    #             print('THAT AREA')
    #             print(supera.upper_left, supera.lower_right)
    #             line = ''
    #             for i, area in enumerate(supera.areas):
    #                 print(i)
    #                 if i == n:
    #                     for indexh, areah in enumerate(self.horizontals[0].areas):
    #                         if indexh < supera.upper_left[1]:
    #                             # print(areah.v, supera.upper_left[1])
    #                             if areah.v == 0:
    #                                 line += ' ' + u'\U00011894'
    #                             else:
    #                                 line += ' ' + str(areah.v)
    #                             if i in [2, 5]:
    #                                 line += '\n'
    #                     if area.v == 0:
    #                         line += ' ' + u'\U00011894'
    #                     else:
    #                         line += ' ' + str(area.v)
    #                     if i in [2, 5]:
    #                         line += '\n'
    #                 else:
    #                     if area.v == 0:
    #                         line += ' ' + u'\U00011894'
    #                     else:
    #                         line += ' ' + str(area.v)
    #                     if i in [2, 5]:
    #                         line += '\n ' + '  '*supera.upper_left[1]
    #             print(line)

        # check m
        # print(supera.upper_left, supera.lower_right)

    def setup_values_superareas(self, n, m, val, existing, new):
        """Get a list of values in SuperAreas."""
        if n < 3 and m < 3:
            self.superarea[0].values.append(val)
            self.superarea[0].areas.append(
                Area(n, m, val, existing, new=new))
        if n < 3 and m > 2 and m < 6:
            self.superarea[1].values.append(val)
            self.superarea[1].areas.append(
                Area(n, m, val, existing, new=new))
        if n < 3 and m > 5:
            self.superarea[2].values.append(val)
            self.superarea[2].areas.append(
                Area(n, m, val, existing, new=new))
        if n > 2 and n < 6 and m < 3:
            self.superarea[3].values.append(val)
            self.superarea[3].areas.append(
                Area(n, m, val, existing, new=new))
        if n > 2 and n < 6 and m > 2 and m < 6:
            self.superarea[4].values.append(val)
            self.superarea[4].areas.append(
                Area(n, m, val, existing, new=new))
        if n > 2 and n < 6 and m > 5:
            self.superarea[5].values.append(val)
            self.superarea[5].areas.append(
                Area(n, m, val, existing, new=new))
        if n > 5 and m < 3:
            self.superarea[6].values.append(val)
            self.superarea[6].areas.append(
                Area(n, m, val, existing, new=new))
        if n > 5 and m > 2 and m < 6:
            self.superarea[7].values.append(val)
            self.superarea[7].areas.append(
                Area(n, m, val, existing, new=new))
        if n > 5 and m > 5:
            self.superarea[8].values.append(val)
            self.superarea[8].areas.append(
                Area(n, m, val, existing, new=new))

    def setup_values(self, horizontals):
        """Fill the sudoku with existing values and ZEROS."""
        for n, h in enumerate(horizontals):
            # run through m
            for m, val in enumerate(h.split()):
                value = int(val)
                if value != 0:
                    existing = True
                    self.counts[value-1] += 1
                    new = False
                else:
                    existing = False
                    self.missing_areas.append((n, m))
                    new = True
                # print(self.counts)
                self.horizontals[n].areas.append(
                    Area(n, m, value, existing, new=new))
                self.verticals[m].areas.append(
                    Area(n, m, value, existing, new=new))
                self.setup_values_superareas(n, m, value, existing, new)
        for i in range(9):
            self.horizontals[i].make_value_list()
            self.verticals[i].make_value_list()

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
        # print('order:', order)
        # print('count:', self.counts)
        return order

    def get_boundary(self, this):
        """Bounderies for horizontal- and verticals by SuperAreas."""
        return (self.superarea[this].upper_left[0],
                self.superarea[this].upper_left[1])
        # return ((self.superarea[this].upper_left[0],
        #          self.superarea[this].lower_right[0]),
        #         (self.superarea[this].upper_left[1],
        #          self.superarea[this].lower_right[1]))

    def make_value_list(self):
        for i in range(9):
            self.horizontals[i].make_value_list()
            self.verticals[i].make_value_list()

    def add_possibilities(self, n, m, number, i):
        self.horizontals[n].areas[m].possibility.append(number)
        self.verticals[m].areas[n].possibility.append(number)
        # print(self.horizontals[n].areas[m].possibility, self.verticals[m].areas[n].possibility)
        # print((n), (m), self.horizontals[n].areas[m].possibility)
        # if i > 0:
        # print(self.superarea[i].areas[n*3+m])
        self.superarea[i].amount[number-1] += 1
        index = (m % 3)+3*(n % 3)
        # print('Index of SuperareaListArea:', index)
        self.superarea[i].areas[index].possibility.append(number)
        # for area in self.superarea[i].areas:
        #     if m == area.m and n == area.n:
        #         area.possibility.append(number)
        #         print(area.n, area.m, area.possibility)
        #         print(n, m, self.superarea[i].areas[index].possibility)

    def remove_possibilities(self, n, m, area_nr, clear=True):
        """Remove the possibilities for one area."""
        if clear:
            self.missing_areas.remove((n, m))
        # print('Removed in', n, m, self.horizontals[n].areas[m].possibility,
        #       self.verticals[m].areas[n].possibility)
        self.horizontals[n].areas[m].possibility = []
        self.verticals[m].areas[n].possibility = []
        index = (m % 3)+3*(n % 3)
        self.superarea[area_nr].areas[index].possibility = []

    def remove_all_possibilities(self):
        """Remove the possibilities for all areas."""
        for index in range(9):
            # print('Superarea:', index)
            for area in self.superarea[index].areas:
                # print('check area')
                # print(area.m, area.n)
                self.remove_possibilities(area.n, area.m, index, clear=False)

    def set_value(self, n, m, number, each):
        index = (n-self.superarea[each].upper_left[0])*3+(
            m-self.superarea[each].upper_left[1])

        self.superarea[each].values[index] = number
        self.superarea[each].areas[index].v = number
        self.horizontals[n].areas[m].v = number
        self.verticals[m].areas[n].v = number
        self.superarea[each].areas[index].is_new = False
        self.horizontals[n].areas[m].is_new = False
        self.verticals[m].areas[n].is_new = False

    def set_count_amount(self, each, index):
        self.superarea[each].amount[index] = 0
        self.counts[index] += 1

    def fill_values_order(self, each):
        # print('fill_values_order')
        # print(each)
        # print('amount:', self.superarea[each].amount)
        for index, count in enumerate(self.superarea[each].amount):
            number = index + 1
            if count == 1:
                print('fill in:', number, 'in SuperArea', each)
                if number not in self.superarea[each].values:
                    self.set_count_amount(each, index)
                    # print('In SuperArea', each, 'set number', number)
                    hori_boundary, verti_boundery = self.get_boundary(each)
                    # print(hori_boundary, verti_boundery)
                    for n in range(hori_boundary, hori_boundary+3):
                        if number not in self.horizontals[n].values:
                            # print('n', n)
                            for m in range(verti_boundery, verti_boundery+3):
                                if not self.horizontals[n].areas[m].is_fix:
                                    if number not in self.verticals[m].values:
                                        # print('\t@', '(', m, ',', n, ')')
                                        # check and update !!

                                        # print('Horizont n,m,p --', self.horizontals[n].areas[m].n,
                                        # self.horizontals[n].areas[m].m, self.horizontals[n].areas[m].possibility,
                                        # self.superarea[each].values)
                                        self.set_value(n, m, number, each)

                                        # Remove the
                                        self.remove_possibilities(n, m, each)

    def run_order(self):
        """
        Run through each SuperArea.

        Check horizontl- and verticals.
        """
        # clear possibilities
        self.remove_all_possibilities()
        # self.display_horizontals()
        # self.display_verticals()
        # print(self.missing_areas)
        # print(len(self.missing_areas))
        # return
        for number in self.get_order():
            # print('searched:', number)
            for i in range(9):
                self.superarea[i].amount[number-1] = 0
                # print('Area number:', i, self.superarea[i].values)
                if number not in self.superarea[i].values:
                    # print('SuperArea', i, 'has no number', number)
                    hori_boundary, verti_boundery = self.get_boundary(i)
                    # print(hori_boundary, verti_boundery)
                    for n in range(hori_boundary, hori_boundary+3):
                        if number not in self.horizontals[n].values:
                            # print('n', n)
                            for m in range(verti_boundery, verti_boundery+3):
                                if not self.horizontals[n].areas[m].is_fix:
                                    if number not in self.verticals[m].values:
                                        # print('m', m)
                                        self.add_possibilities(n, m, number, i)

                # print('For the number:', number)
                # print('---')
                self.fill_values_order(i)
        self.make_value_list()

    def run(self):
        """Solve it."""
        first = 1
        second = 0
        i = 0
        while first != second:
            first = len(self.missing_areas)
            self.run_order()
            second = len(self.missing_areas)
            print(first, second)
            i += 1
            print(i)


def poiting_pair(numbers, superarea, index):
    """Find poitning pairs."""
    print(numbers, 'is the set of SupAr:', index, '\n', superarea)
    print(superarea.amount)
    # for i in numbers:
    #     print('check if', i+1,)
    for a in superarea.amount:
        if a / 2 == 1:
            print('Amount of', a)

    for area in superarea.areas:
        # all not set areas:
        # if not area.is_fix and area.is_new:
        if area.is_new:
            print(index, '- poissibilities:', area.possibility)
            # print(area, '\n')
            print(area.is_new)
            print(f"({area.n},{area.m})\n")
            # print('Area posibilities:', f'of position {i} on',
            #       f'({area.n}, {area.m})', area.possibility)
            # [all_numbers.append(i) for i in area.possibility]

    print(superarea.areas[8].possibility)
    print(superarea.areas[5].possibility)


def main():
    """Run this in direct call."""
    # display(sudoku_71())
    print('main(): Ω Ω Ω - z')

    h1 = '9 6 0 0 0 0 2 0 0'
    h2 = '0 7 0 5 9 2 0 0 0'
    h3 = '0 0 0 8 0 0 0 0 0'
    h4 = '0 2 0 0 0 0 7 0 8'
    h5 = '0 0 8 0 0 0 9 0 0'
    h6 = '1 0 3 0 0 0 0 5 0'
    h7 = '0 0 0 0 0 6 0 0 0'
    h8 = '0 0 0 9 1 4 0 2 0'
    h9 = '0 0 2 0 0 0 0 4 6'

    h_test1 = [h1, h2, h3, h4, h5, h6, h7, h8, h9]

    s = Sudoku('medium')
    print(s.difficulty)

    s.setup_values(h_test1)

    for n, (h, vert) in enumerate(zip(s.horizontals, s.verticals)):
        for m, (a, b) in enumerate(zip(h.areas, vert.areas)):
            # print('test1:', n, m, a.v)
            assert a.v == int(h_test1[n].split()[m])
            assert b.v == int(h_test1[m].split()[n])

    # s.display()
    #
    s.run()  #
    #
    # s.display_superarea_amount()
    # #
    # s.display()

    # print('\t', s.horizontals[0].values)
    # print('\t', s.horizontals[1].values)
    # print('\t', s.horizontals[2].values)
    # print()
    # print('\t', s.verticals[8].values)
    # print('\t', s.verticals[7].values)
    # print('\t', s.verticals[6].values)

    # s.display_superarea_amount()

    for n, (h, vert) in enumerate(zip(s.horizontals, s.verticals)):
        for m, (a, b) in enumerate(zip(h.areas, vert.areas)):
            if a.is_new:
                ...
                # print(a.n, a.m, a.possibility)
                # print(a.n, a.m, a.possibility)

    for index in range(2, 3):
        all_numbers = []
        print('Superarea Values:', s.superarea[index].values)
        print('Superarea Amount of each', s.superarea[index].amount)
        hori_boundary, verti_boundery = s.get_boundary(index)
        print('Superarea Upper_Left', hori_boundary, verti_boundery)
        for i, area in enumerate(s.superarea[index].areas):
            if area.is_new:
                print('Area posibilities:\n\t', f'of {i} on',
                      f'({area.n}, {area.m})', area.possibility)
                [all_numbers.append(i) for i in area.possibility]

        poiting_pair(set(all_numbers), s.superarea[index], index)

    # for superarea in s.superarea:
    #     # print(superarea.amount)
    #     for area in superarea.areas:
    #         if not area.is_fix and area.n < 3 and area.m < 3:
    #             print('area-vale', superarea.values)
    #             # print(area.is_new)
    #             print(area.possibility, ' ', area.n, area.m, ' - ', area.is_fix)
    #     if not a.is_new and a.n < 3 and a.m < 3:
    #         # check if there are values in superarea which just have one n or m:
    #         # if len(a.possibility) < 5:
    #         ...
        # print(a.possibility, ' ', a.n, a.m, ' - ', a.is_fix)

    # print()
    # s.display_horizontals(0)
    # s.display_superarea(2)
    # s.display_verticals(8)


if __name__ == "__main__":
    main()
