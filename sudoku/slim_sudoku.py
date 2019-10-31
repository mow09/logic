"""Sudoku solver."""


class Area:
    """One area of 81 areas in a sudoku."""

    def __init__(self, n, m, v, fix, sa=10, new=True):
        """Initiale position, value."""
        print('INITIAL AREA')

        self.n = n
        self.m = m
        self.v = v
        self.sa = sa
        self.possibility = []
        self.is_fix = fix
        self.is_new = new

    def __str__(self):
        """Show functions."""
        return f"""\nArea\tcall n: {self.n}, m: {self.m}, v: {self.v}\n\
            is_fix: {self.is_fix}, \n\tis_new: {self.is_new}\n\
                possibility: {self.possibility}\n"""

    def __repr__(self):
        """Show results."""
        return f"n: {self.n}, \nm: {self.m}, \nv: {self.v}, \n\
            is_fix: {self.is_fix}, \nis_new: {self.is_new}, \n\
                possibility: {self.possibility}"


def main():
    """Run in dirct call."""
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


if __name__ == "__main__":
    main()
