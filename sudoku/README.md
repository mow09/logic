# SUDOKU
Sudoku
## Classes
```python
class Area
class SuperArea
class Horizontal
class Sudoku
```
### Areas
An area is a position `(n, m)` in the matrix.

### Superarea
Superareas are on this coordinates.

id  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8
--- | --- | --- | --- | --- | --- | ---  | ---  | ---  | ---
begin | (0,0) | (0,3)| (0,6)  | (3,0)  |  (3,3) | (3,6) | (6,0) | (6,3) | (6,6)
end   | (2,2) | (2,5) | (2,8) |  (5,3)| (5,5) | (5,8) | (8,3) | (8,3)| (8,8)

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
