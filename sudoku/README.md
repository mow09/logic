# SUDOKU
Sudoku
## Classes
```python
Area()
SuperArea()
Horizontal()
Sudoku()
```
### Areas
An area is a position `(n, m)` in the matrix.

### Superarea
Superareas are on this coordinates.

id | begin | end
--- | --- | ---
0 | (0,0) | (2,2)
1 | (0,3) | (2,5)
2 | (0,6) | (2,8)
3 | (3,0) | (5,3)
4 | (3,3) | (5,5)
5 | (3,6) | (5,8)
6 | (6,0) | (8,3)
7 | (6,3) | (8,3)
8 | (6,6) | (8,8)

### Horizontal
Horizontals are from
`(n, 0) to (n, 8)` with `n={0,1...,8}`.
`n` is also the id of the horizontal.
### Vertical
Verticals are from
`(1, m) to (8, m)` with `m={0,1...,8}`.
`m` is also the id of the vertical.

### Sudoku
That class is for the solving.

## Example

    9 6 - | - - - | 2 - -
    - 7 - | 5 9 2 | - - -
    - - - | 8 - - | - - -
    ------+-------+------
    - 2 - | - - - | 7 - 8
    - - 8 | - - - | 9 - -
    1 - 3 | - - - | - 5 -
    ------+-------+------
    - - - | - - 6 | - - -
    - - - | 9 1 4 | - 2 -
    - - 2 | - - - | - 4 6


## TODO:
- [ ] put main content into a test file
- [ ] add all modules after it is solving
- [ ] run speed test
