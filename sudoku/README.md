# SUDOKU
Sudoku
## Classes
```python
class Area
class SuperArea
class Horizontal
class Sudoku
```
### Area
An area is a position `(.n, .m)` in the matrix which contains (has following attributes:) a value `.v` (zero when no number is placed), the numbers that can be on that position `.possibilities` it `.is_fix` when the value was given as a starting point, `.is_new` will be set `False` after a number/value is placed. Also an area know in which superarea (`.sa`) it is.

Hint: The `n` / `m` of an area is the ID of horizontal / vertical.
### Upper Classes
The following classes exist to modify areas
#### Superarea
`.values` contains the list of existing values/numbers which are fix or were placed. It has a specific order (see bottom of this subsection). `.areas` is a list of all 81 areas (`Area()`). They are set simultaneous for superarea, horizontal and vertical. So it is ensured that a change on an area will change in all _upper classes_. The attribute `.amount` counts how often a value is possible.

Hint: If a number has an amount ((position+1=number) in array) of one it can be set/placed.

Superareas are on following coordinates.

ID    |       0 |       1 |       2 |        3 |       4 |       5 |       6 |       7 |   8
  --- |     --- |     --- |     --- |      --- |     --- |     --- |    ---  |    ---  | --- 
begin | `(0,0)` | `(0,3)` | `(0,6)` | `(3,0)`  | `(3,3)` | `(3,6)` | `(6,0)` | `(6,3)` | `(6,6)`
end   | `(2,2)` | `(2,5)` | `(2,8)` |  `(5,3)` | `(5,5)` | `(5,8)` | `(8,3)` | `(8,3)` | `(8,8)`

Area ID goes from top left to bottom right. ID goes from `0:(n, m)` to `1:(n, m+1)`, `2:(n, m+2)`, `3:(n+1, m)` up to ... `8:(n+2, m+2)`

#### Horizontal
`.areas` `.values` and `.amount` as in superarea.

Horizontals are from
`(n, 0) to (n, 8)` with `n = {0,1...,8}`.
`n` is also the ID of the horizontal. E.g. `area.n` - ! not `.areas`
#### Vertical
`.areas` `.values` and `.amount` as in superarea.

Verticals are from
`(1, m) to (8, m)` with `m = {0,1...,8}`.
`m` is also the ID of the vertical. E.g. `area.m` - ! not `.areas`

## Sudoku
That class is for solving sudokus. It has the following list attributes to get information:
- `.horizontals`
- `.verticals`
- `.superareas`

`counts` counts how often a value is already set. This is used to get an order. A often placed number might be set easier.

`missing_areas` contains all missing areas by a tuple of (n, m).

---
`.setup()` (`set_value()`)
`.target_amount()`
`.pointing_pair()`

### Setup
- set_number()

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
- [x] `.target_amount()` works

- [ ] implement tests

---
- [ ] the `.amount` of all upper classes is set to 9 and has to be changed that it works again with order.
    - [ ] check if number is set in value for each - like amount!
    - [ ] check `set_value(setup=False)`
    - amounts:
        - [ ] superarea = 0
        - [ ] horizontal = 0
        - [ ] vertical = 0
    - [ ] area
        - [ ] value = number
        - [ ] possibilities =[]
    - [ ] counts

- [ ] the `run()` method is changed and has to be reimplemented with the focus of `setup` and recallable functions.

---
- [ ] ~~setup Travis~~
- [ ] clean unused code (overworked)
- [ ] put main content into a test file
- [ ] add all modules after it is solving
- [ ] run speed test
