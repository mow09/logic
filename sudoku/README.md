### Sudoku logic in general to use it for image processing.

## TODO
- [x] verticals
- [x] horizontals
- [x] superarea class
- [x] horizontal/vertical class
- [ ] run_order
    - where to save the possibilities and how to modify those areas in the sudoku class
- [ ] final algo, test

"""
9x9
2 or 3 types of areas:
main area all: (0,0) -> (8,8)
n x m

linear areas: (top - down)
(0,0) -> (0,8)
(1,0) -> (1,8)
(2,0) -> (2,8)
(3,0) -> (3,8)
(4,0) -> (4,8)
(5,0) -> (5,8)
(6,0) -> (6,8)
(7,0) -> (7,8)
(8,0) -> (8,8)

linear areas: (left - right)
(0,0) -> (8,0)
(0,1) -> (8,1)
(0,2) -> (8,2)
(0,3) -> (8,3)
(0,4) -> (8,4)
(0,5) -> (8,5)
(0,6) -> (8,6)
(0,7) -> (8,7)
(0,8) -> (8,8)

---

```python
class Area:
    # is a number between [1,..,9]
    # exists 9x9 times
class Horizontal:
    # contains numbers from [1,..,9]
    # exists 9 times
class Vertical:
    # contains numbers from [1,..,9]
    # exists 9 times
class Square:
    # contains numbers from [1,..,9]
    # exists 9 times
class Sudoku:
    # contains 9 x numbers from [1,..,9]
    # exists 9 times
```
---

square areas:
(0,0) -> (2,2)
(0,3) -> (2,5)
(0,6) -> (2,8)
(3,0) -> (5,3)
(3,3) -> (5,5)
(3,6) -> (5,8)
(6,0) -> (8,3)
(6,3) -> (8,3)
(6,6) -> (8,8)

two kinds of fields:
1. it's fix
2. flexible - can be changed to fit it

EXAMPLE - clever sodoku - mittle - 77:
fix values:

(n0,m0), (n0,m1), (n0,m2), |   (6),     (9),   (n0,m5), | (n0,m6), (n0,m7),  (n0,m8)
(n1,m0), (n1,m1),   (6),   | (n1,m3), (n1,m4), (n1,m5), |   (8),     (4),      (3)
(n2,m0), (n2,m1),   (2),   |   (8),   (n2,m4), (n2,m5), | (n2,m6), (n2,m7),    (7)

(n3,m0), (n3,m1), (n3,m2), | (n3,m3), (n3,m4), (n3,m5), |   (4),   (n3,m7),    (1)
  (7),   (n4,m1), (n4,m2), |   (2),   (n4,m4),   (5),   | (n4,m6), (n4,m7),    (6)
  (5),   (n5,m1),   (3),   | (n5,m3), (n5,m4), (n5,m5), | (n5,m6), (n5,m7),  (n5,m8)

  (6),   (n6,m1), (n6,m2), | (n6,m3), (n6,m4),   (7),   |   (5),   (n6,m7),  (n6,m8)
  (8),     (7),     (5),   | (n7,m3), (n7,m4), (n7,m5), |   (9),   (n7,m7),  (n7,m8)
(n8,m0), (n8,m1), (n8,m2), | (n8,m3),   (3),     (4),   | (n8,m6), (n8,m7),  (n8,m8)

---

(n0,m0), (n0,m1), (n0,m2), | (n0,m3), (n0,m4), (n0,m5), | (n0,m6), (n0,m7),  (n0,m8)
(n1,m0), (n1,m1), (n1,m2), | (n1,m3), (n1,m4), (n1,m5), | (n1,m6), (n1,m7),  (n1,m8)
(n2,m0), (n2,m1), (n2,m2), | (n2,m3), (n2,m4), (n2,m5), | (n2,m6), (n2,m7),  (n2,m8)

(n3,m0), (n3,m1), (n3,m2), | (n3,m3), (n3,m4), (n3,m5), | (n3,m6), (n3,m7),  (n3,m8)
(n4,m0), (n4,m1), (n4,m2), | (n4,m3), (n4,m4), (n4,m5), | (n4,m6), (n4,m7),  (n4,m8)
(n5,m0), (n5,m1), (n5,m2), | (n5,m3), (n5,m4), (n5,m5), | (n5,m6), (n5,m7),  (n5,m8)

(n6,m0), (n6,m1), (n6,m2), | (n6,m3), (n6,m4), (n6,m5), | (n6,m6), (n6,m7),  (n6,m8)
(n7,m0), (n7,m1), (n7,m2), | (n7,m3), (n7,m4), (n7,m5), | (n7,m6), (n7,m7),  (n7,m8)
(n8,m0), (n8,m1), (n8,m2), | (n8,m3), (n8,m4), (n8,m5), | (n8,m6), (n8,m7),  (n8,m8)
"""

## Speed Test
How to implement what.

### comparison conditions

```python
(1) if (j+1) % 3 == 0 and j != 8:
(2) if j in [2, 5]:
```
Nummer (2) ist schneller in `display()`:
```
63.5 µs ± 862 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)
55.9 µs ± 403 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)
```

### numpy or list in list ?!
