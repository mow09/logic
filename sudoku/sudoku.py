"""Sudoku AI."""


class Area:
    """One area of 81 areas in a sudoku."""

    def __init__(self, n, m, v, fix, sa=10, new=True):
        """Initiale position, value."""
        print('INITIAL AREA')

        self.n = n
        self.m = m
        self.v = v
        self.sa = sa
        self.possibilities = []
        self.is_fix = fix
        self.is_new = new

    def __str__(self):
        """Show functions."""
        return f"""\nArea\tcall n: {self.n}, m: {self.m}, v: {self.v}\n\
            is_fix: {self.is_fix}, \n\tis_new: {self.is_new}\n\
                possibilities: {self.possibilities}\n"""

    def __repr__(self):
        """Show results."""
        return f"n: {self.n}, \nm: {self.m}, \nv: {self.v}, \nis_fix: {self.is_fix}, \nis_new: {self.is_new}, \npossibilities: {self.possibilities}"


class SuperArea:
    """One SuperArea contains nine Areas."""

    def __init__(self, upper_left, lower_right):
        """Initale the SuperArea."""
        print('INITIAL SUPERAREA')
        self.upper_left = upper_left
        self.lower_right = lower_right
        self.areas = []
        # contains existing-numbers in the expressive position for this class
        self.values = []
        # returns how often it is
        self.amount = [9, 9, 9, 9, 9, 9, 9, 9, 9]

    def __repr__(self):
        """Show results."""
        return f"SuperArea()\n\tupper_left: {self.upper_left}, \n\tlower_right: {self.lower_right}, \n\tareas: List(Area()), \n\tvalues: {self.values}, \n\tamount: {self.amount}"


class Horizontal:
    """Nine horizontal lines."""

    def __init__(self):
        """Parameter of horizontal line."""
        print('INITIAL HORIZONTAL')
        self.areas = []
        # contains existing-numbers in the expressive position for this class
        self.values = []
        self.amount = [9, 9, 9, 9, 9, 9, 9, 9, 9]

    def make_value_list(self):
        """Make a list of the values."""
        self.values = []
        if len(self.values) == 0:
            for i in range(9):
                self.values.append(self.areas[i].v)

    def __repr__(self):
        """Show results."""
        return f"Horizontal \n\tvalues: {self.values}"


class Vertical:
    """Nine vertical lines."""

    def __init__(self):
        """Parameter of vertical line."""
        print('INITIAL VERTICAL')
        self.areas = []
        # contains existing-numbers in the expressive position for this class
        self.values = []
        self.amount = [9, 9, 9, 9, 9, 9, 9, 9, 9]

    def make_value_list(self):
        """Make a list of the values."""
        if len(self.values) != 0:
            self.values = []
        for i in range(9):
            self.values.append(self.areas[i].v)

    def __repr__(self):
        """Show results."""
        return f"Vertical \n\tvalues: {self.values}"


class Sudoku:
    """The class solves the sudoku."""

    def __init__(self, difficulty):
        """Set the difficulty."""
        print('INITIAL SUDOKU')
        self.difficulty = difficulty

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
        self.superareas = [SuperArea((0, 0), (2, 2)),
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
            for c, i in enumerate(self.superareas[index].amount):
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
        print()
        for j, h in enumerate(self.horizontals):
            line = '\t\t\t'
            for i, area in enumerate(h.areas):
                if not isinstance(area, int):
                    value = area.v
                if value == 0:
                    line += ' ' + '-'
                else:
                    if area.is_fix:
                        line += ' ' + str(value)
                    else:
                        line += '.' + str(value)
                if i in [2, 5]:
                    line += ' |'

            print(line)
            if j in [2, 5]:
                print('\t\t\t-------+-------+-------')
        print('')
        print('\t\t\t\t\t\t\t',  'V', ' is old')
        print('\t\t\t\t\t\t\t', u'\U00011894', ' is missing')
        print('\t\t\t\t\t\t\t', '.V', 'is entered')
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

    def display_verticals(self, spec=False):
        """Display the vertical lines."""
        if not spec:
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
            # stores the key for #verticals and their possibilities
            dict_store = {}
            for key in spec:
                dict_store[key] = self.verticals[key]
            # h = self.verticals[spec]
            print(dict_store)
            for key in dict_store:
                # print('\t', 'Area', key)
                line = '\t\t\n\n'
                for i, area in enumerate(dict_store[key].areas):
                    if area.v == 0:
                        line += u'\t\t\U00011894' + f'\t{area.possibilities}\n'
                    else:
                        line += '\t\t' + str(area.v) + '\n'
                    if i in [2, 5]:
                        line += '\n'
                print(line+'\n\n')

    def display_superarea(self, spec):
        """Display one superarea lines."""
        h = self.superareas[spec]
        line = '\t'
        for i, area in enumerate(h.areas):
            if area.v == 0:
                line += '\t' + u'\U00011894'
            else:
                line += '\t' + str(area.v)
            if i in [2, 5]:
                line += '\n\t'
        print(line)

    def setup_values_superareas(self, n, m, val, area_set):
        """Get a list of values in SuperAreas."""
        print('SETUP_VALUES_SUPERAREAS')
        if n < 3 and m < 3:
            self.superareas[0].values.append(val)
            self.superareas[0].areas.append(area_set)
            area_set.sa = 0
        if n < 3 and m > 2 and m < 6:
            self.superareas[1].values.append(val)
            self.superareas[1].areas.append(area_set)
            area_set.sa = 1
        if n < 3 and m > 5:
            self.superareas[2].values.append(val)
            self.superareas[2].areas.append(area_set)
            area_set.sa = 2
        if n > 2 and n < 6 and m < 3:
            self.superareas[3].values.append(val)
            self.superareas[3].areas.append(area_set)
            area_set.sa = 3
        if n > 2 and n < 6 and m > 2 and m < 6:
            self.superareas[4].values.append(val)
            self.superareas[4].areas.append(area_set)
            area_set.sa = 4
        if n > 2 and n < 6 and m > 5:
            self.superareas[5].values.append(val)
            self.superareas[5].areas.append(area_set)
            area_set.sa = 5
        if n > 5 and m < 3:
            self.superareas[6].values.append(val)
            self.superareas[6].areas.append(area_set)
            area_set.sa = 6
        if n > 5 and m > 2 and m < 6:
            self.superareas[7].values.append(val)
            self.superareas[7].areas.append(area_set)
            area_set.sa = 7
        if n > 5 and m > 5:
            self.superareas[8].values.append(val)
            self.superareas[8].areas.append(area_set)
            area_set.sa = 8

    def get_order(self):
        """Return a list sorted by amount."""
        # print('GET_ORDER')
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
        # print('GET_BOUDARY')
        return (self.superareas[this].upper_left[0],
                self.superareas[this].upper_left[1])

    def make_value_list(self):
        print('MAKE_VALUE_LIST')
        for i in range(9):
            self.horizontals[i].make_value_list()
            self.verticals[i].make_value_list()

    def get_placed_values(self, area):
        """Return placed values focusing an Area."""
        return set(self.horizontals[area.n].values +
                   self.verticals[area.m].values +
                   self.superareas[area.sa].values)

    def add_amount(self):
        """Add the amount of the possibilities of number in a SuperArea."""
        for superarea in self.superareas:
            for number in range(1, 10):
                # counter = 0
                for area in superarea.areas:
                    if number in area.possibilities:
                        if number not in superarea.values:
                            superarea.amount[number-1] += 1

    def add_possibilities(self):
        """Add the possibilities for each Area - setup."""
        for superarea in self.superareas:
            for area in superarea.areas:
                if area.n == 8 and area.m == 0:
                    print()
                    print()
                    print('runs in setup')
                    print()
                if not area.is_fix and area.is_new:
                    print('IS NEW', area.is_new)
                    for number in range(1, 10):
                        if number not in self.get_placed_values(area):
                            if area.n == 6 and area.m == 0:
                                print((self.get_placed_values(area)))
                            area.possibilities.append(number)
                            if area.n == 6 and area.m == 0:
                                print(area.possibilities)

    def set_value(self, n, m, number, each):
        """Set number in spacific position for SA,H,V - setup."""
        index = (n-self.superareas[each].upper_left[0])*3+(
            m-self.superareas[each].upper_left[1])
        print('\t#', number, 'in SuperArea', each, 'with (n,m)', n, m)
        print('\tArea Possibilities',
              self.superareas[each].areas[index].possibilities, '\n')
        if number in self.superareas[each].areas[index].possibilities:
            self.superareas[each].values[index] = number
            self.superareas[each].areas[index].v = number
            self.horizontals[n].areas[m].v = number
            self.horizontals[n].values[m] = number
            self.verticals[m].areas[n].v = number
            self.verticals[m].values[n] = number
            self.superareas[each].areas[index].is_new = False
            self.horizontals[n].areas[m].is_new = False
            self.verticals[m].areas[n].is_new = False

            for area_h, area_v in zip(self.horizontals[n].areas,
                                      self.verticals[m].areas):
                if number in area_h.possibilities:
                    area_h.possibilities.remove(number)
                if number in area_v.possibilities:
                    area_v.possibilities.remove(number)

    def setup_values(self, horizontals):
        """Fill the sudoku with existing values and ZEROS."""
        print('SETUP_VALUES - horizontal entered')
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
                area_set = Area(n, m, value, existing, new=new)
                self.horizontals[n].areas.append(area_set)
                self.verticals[m].areas.append(area_set)
                self.setup_values_superareas(n, m, value, area_set)
        for i in range(9):
            self.horizontals[i].make_value_list()
            self.verticals[i].make_value_list()
        print('\n\n\t\tSudokus setup_values() done\n\n')

        # here should come the possibilities#s#s
        self.add_possibilities()
        self.add_amount()

    def info(self):
        """Get info about the sudoku at this time."""
        print('\nINFOBOARD:')
        print('\tSUPERAREA:')
        print('\t\tSuperarea\tPlaced\tMissing')
        missing_values_all = [i+1 for i in range(9)]*9
        missing_values_all_h = [i+1 for i in range(9)]*9
        missing_values_all_v = [i+1 for i in range(9)]*9
        for i, superarea in enumerate(self.superareas):
            missing_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            counter = 0
            for value in superarea.values:
                if value > 0:
                    counter += 1
                    # print(missing_values, value, superarea.values)
                    missing_values.remove(value)
                    missing_values_all.remove(value)
            print(f'\t\t\t{i}\t{counter}\t{missing_values}')
        print('\tHORIZONTAL:')
        print('\t\t\tn\tPlaced\tMissing')
        for i, hori in enumerate(self.horizontals):
            # missing_values_all = [i+1 for i in range(9)]*9
            missing_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            counter = 0
            for value in hori.values:
                if value > 0:
                    counter += 1
                    # print(missing_values, value, superarea.values)
                    missing_values.remove(value)
                    missing_values_all_h.remove(value)
            print(f'\t\t\t{i}\t{counter}\t{missing_values}')
        print('\tVERTICALS:')
        print('\t\t\tm\tPlaced\tMissing')
        for i, verti in enumerate(self.verticals):
            # missing_values_all = [i+1 for i in range(9)]*9
            missing_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            counter = 0
            for value in verti.values:
                if value > 0:
                    counter += 1
                    # print(missing_values, value, superarea.values)
                    missing_values.remove(value)
                    missing_values_all_v.remove(value)
            print(f'\t\t\t{i}\t{counter}\t{missing_values}')

        print('\tSUMMERY:')
        counter = 81
        one, two, three, four, five, six, seven, eight, nine = [9]*9
        for i, val in enumerate(missing_values_all):
            counter -= 1
            if val == 1:
                one -= 1
            elif val == 2:
                two -= 1
            elif val == 3:
                three -= 1
            elif val == 4:
                four -= 1
            elif val == 5:
                five -= 1
            elif val == 6:
                six -= 1
            elif val == 7:
                seven -= 1
            elif val == 8:
                eight -= 1
            elif val == 9:
                nine -= 1
            else:
                print('Error')

        counter_h = 81
        one_h, two_h, three_h, four_h, five_h, six_h, seven_h, eight_h, nine_h = [9]*9
        for i, val in enumerate(missing_values_all_h):
            counter_h -= 1
            if val == 1:
                one_h -= 1
            elif val == 2:
                two_h -= 1
            elif val == 3:
                three_h -= 1
            elif val == 4:
                four_h -= 1
            elif val == 5:
                five_h -= 1
            elif val == 6:
                six_h -= 1
            elif val == 7:
                seven_h -= 1
            elif val == 8:
                eight_h -= 1
            elif val == 9:
                nine_h -= 1
            else:
                print('Error')

        counter_v = 81
        one_v, two_v, three_v, four_v, five_v, six_v, seven_v, eight_v, nine_v = [9]*9
        for i, val in enumerate(missing_values_all_v):
            counter_v -= 1
            if val == 1:
                one_v -= 1
            elif val == 2:
                two_v -= 1
            elif val == 3:
                three_v -= 1
            elif val == 4:
                four_v -= 1
            elif val == 5:
                five_v -= 1
            elif val == 6:
                six_v -= 1
            elif val == 7:
                seven_v -= 1
            elif val == 8:
                eight_v -= 1
            elif val == 9:
                nine_v -= 1
            else:
                print('Error')
        print('\t\tmissing in total:\t', len(missing_values_all),
              len(missing_values_all_h), len(missing_values_all_v))
        print('\t\tplaced in total:\t', counter, counter_h, counter_v)
        print('\t\tmissing in one:\t\t', one, one_h, one_v)
        print('\t\tmissing in two:\t\t', two, two_h, two_v)
        print('\t\tmissing in three:\t', three, three_h, three_v)
        print('\t\tmissing in four:\t', four, four_h, four_v)
        print('\t\tmissing in five:\t', five, five_h, five_v)
        print('\t\tmissing in six:\t\t', six, six_h, six_v)
        print('\t\tmissing in seven:\t', seven, seven_h, seven_v)
        print('\t\tmissing in eight:\t', eight, eight_h, eight_v)
        print('\t\tmissing in nine:\t', nine, nine_h, nine_v)
        # print(missing_values_all)
        print()

    def run_target(self):
        """
        Run through each SuperArea.

        Check horizontl- and verticals.
        """
        print('\n\n###\n\tREDESIGNED TARGET\n')
        for number in self.get_order():
            # print('searched:', number)
            for i, superarea in enumerate(self.superareas):
                # self.superareas[i].amount[number-1] = 0
                if superarea.amount[number-1] == 1:
                    # print(number, '-', superarea.amount[number-1])
                    for area in superarea.areas:
                        if number in area.possibilities:
                            index = (area.n-superarea.upper_left[0])*3+(
                                area.m-superarea.upper_left[1])
                            # delete all possibilities
                            area.possibilities = []
                            area.is_new = False
                            area.v = number
                            # set amount
                            superarea.amount[number-1] = 0
                            superarea.values[index] = number
                            self.horizontals[area.n].values[area.m] = number
                            self.verticals[area.m].values[area.n] = number

                            # set value in all 3
                            self.missing_areas.remove((area.n, area.m))

                            # clean all areas in n and m and if in also the number
                            for area_h, area_v in zip(self.horizontals[area.n].areas, self.verticals[area.m].areas):
                                if number in area_h.possibilities:
                                    area_h.possibilities.remove(number)
                                    self.superareas[area_h.sa].amount[number-1] -= 1
                                if number in area_h.possibilities:
                                    area_v.possibilities.remove(number)
                                    self.superareas[area_v.sa].amount[number-1] -= 1

    def clean_amount(self, supers, number, norm, m=False):
        """Decrement the amount if that number."""
        for i in supers:
            for area in(self.superareas[i].areas):
                if area.is_new:
                    if m:
                        if area.m == norm:
                            if number in area.possibilities:
                                self.superareas[i].amount[number-1] -= 1
                                area.possibilities.remove(number)
                                # print('M:', area.possibilities,
                                #       self.superareas[i].amount)
                                # delete the amount of that position/number
                                #
                    else:
                        if area.n == norm:
                            if number in area.possibilities:
                                # print('N:Ω', area.possibilities,
                                #       self.superareas[i].amount)
                                self.superareas[i].amount[number-1] -= 1
                                area.possibilities.remove(number)
                                # print('N:', area.possibilities,
                                #       self.superareas[i].amount)
                                # delete the amount of that position/number

    def clean_n_m(self, numbers, index):
        """Clean n or m. Depending on the pointer."""
        # print('\t\tClean n m')
        # print('\t\t', numbers, 'in SuperArea', index)
        for key in numbers:
            # area_nr = index - 1
            if numbers[key][0] == numbers[key][2]:
                # print('IT is N')
                # is it left
                if index in [0, 3, 6]:
                    # print('clean horizontal in Superarea', index+1, index +
                    #       2, 'the number', key, 'for n', numbers[key][0])
                    self.clean_amount([index+1, index+2], key, numbers[key][0])

                # is it mid
                if index in [1, 4, 7]:
                    # print('clean horizontal in Superarea',  index-1, index +
                    #       1, 'the number', key, 'for n', numbers[key][0])
                    self.clean_amount([index-1, index+1], key, numbers[key][0])
                # is it right
                if index in [2, 5, 8]:
                    # print('clean horizontal in Superarea', index-2, index -
                    #       1, 'the number', key, 'for n', numbers[key][0])
                    self.clean_amount([index-2, index-1], key, numbers[key][0])
            else:
                # print('IT is M')
                # is it top
                if index in [0, 1, 2]:
                    # print('clean vertical in Superarea', index+1*3, index +
                    #       2*3, 'the number', key, 'for m', numbers[key][1])
                    self.clean_amount([index+1*3, index+2*3], key, numbers[key][1], True)
                # is it mid
                if index in [3, 4, 5]:
                    # print('clean vertical in Superarea', index-1*3, index +
                    #       1*3, 'the number', key, 'for m', numbers[key][1])
                    self.clean_amount([index-1*3, index+1*3], key, numbers[key][1], True)
                # is it down
                if index in [6, 7, 8]:
                    # print('clean vertical in Superarea', index-2*3, index -
                    #       1*3, 'the number', key, 'for m', numbers[key][1])
                    self.clean_amount([index-2*3, index-1*3], key, numbers[key][1], True)

    def pointing_pair(self):
        """Find poitning pairs."""
        print('Pointing Pair')
        for index in range(9):
            numbers = {}
            # check pointing pair for each number which is not in that superarea.
            for i in range(9):
                number = i+1
                # if it is not in that self.superareas[index].
                if number not in self.superareas[index].values:
                    # check if the number is in the area.possibilities
                    # and controlle m and n
                    # print('\nChecking for number', i, 'if it can be a pointing pair in SuperArea', index)
                    # print('\tCheck number', number)
                    for area in self.superareas[index].areas:
                        if area.is_new:
                            if self.superareas[index].amount[i] / 2 == 1:
                                if i+1 in area.possibilities:
                                    if number not in numbers:
                                        numbers[number] = []
                                    numbers[number].append(area.n)
                                    numbers[number].append(area.m)
                                    # print('The amount is exaactly 2! for', number)
                                    # print(f"({area.n},{area.m})\n")
                    # print(numbers)
                    if len(numbers) > 0:
                        # clean nm
                        self.clean_n_m(numbers, index)
                        del numbers[number]

    def run_target_loop(self):
        """Run order/Find direct and hiden targets."""
        print('Run Order Loop')
        first = 1
        second = 0
        i = 0
        while first != second:
            first = len(self.missing_areas)
            self.run_target()
            second = len(self.missing_areas)
            print(first, second)
            i += 1
            print(i)

    def check_info(self):
        """Display some information."""
        # self.display()
        for i, superarea in enumerate(self.superareas):
            if i == 2:
                print("S", superarea.values)  # , superarea.amount)
                for j, area in enumerate(superarea.areas):
                    if j in [4, 5]:
                        print(area.possibilities, '- possibilities')

        print()
        for i, horo in enumerate(self.horizontals):
            if i == 1:
                print("H", horo.values)
                for j, area in enumerate(horo.areas):
                    if j in [7, 8]:
                        print(area.possibilities, '- possibilities')
        print()
        for i, verti in enumerate(self.verticals):
            if i in [7, 8]:
                print("V", verti.values)
                for j, area in enumerate(verti.areas):
                    if j is 1:
                        print(area.possibilities, '- possibilities')

        for i, superarea in enumerate(self.superareas):
            if i == 2:
                print("S", superarea.values)  # , superarea.amount)
                for j, area in enumerate(superarea.areas):
                    if area.is_new:
                        print(j, area.possibilities, '- possibilities', area.is_new)
        print()

    def info_superarea(self, spec=False):
        """Display all possibilities."""
        if not spec:
            for i, superarea in enumerate(self.superareas):
                print(f'In SUPERAREA {i}: - {superarea.amount}')
                for j, area in enumerate(superarea.areas):
                    print(f'\t\tIn AREA {j} posibilities', area.possibilities)
                print()
        else:
            for i, superarea in enumerate(self.superareas):
                if i in spec:
                    print(f'In SUPERAREA {i}: - {superarea.amount}')
                    for j, area in enumerate(superarea.areas):
                        print(f'\t\tIn AREA {j} posibilities', area.possibilities)
                    print()

    def info_values(self):
        """Display all values for superarea, horizontal, vertical."""
        for i, superarea in enumerate(self.superareas):
            print(f'In SUPERAREA {i}:')
            for j, area in enumerate(superarea.areas):
                print(f'\t\tIn AREA {j} posibilities', area.possibilities)
            print()

    def run(self):
        """Solve it."""


def main():
    """Latest run."""
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

    s.setup(h_test1)
    s.run()


if __name__ == "__main__":
    main()
