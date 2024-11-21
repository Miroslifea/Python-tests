# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

# Documentation

This library provides functions for calculating area and perimiter of various geometric shapes. The implementation for each shape is located in a separate file.

## Triangle

### Area

`area(a, h)`

Returns area of a triangle with base `a` and height `h`

```
> area(4, 5)
10
```

### Perimiter

`perimiter(a, b, c)`

Returns perimiter of a triangle with sides `a`, `b` and `c`

```
> perimiter(1, 2, 3)
6
```

## Rectangle

### Area

`area(a, b)`

Returns area of a rectangle with sides `a` and `b`

```
> area(4, 3)
12
```

### Perimiter

`perimiter(a, b)`

Returns perimiter of a rectangle with sides `a` and `b`

```
> perimiter(7, 4)
22
```

## Circle

### Area

`area(r)`

Returns area of a circle with radius `r`

```
> area(2)
12.566370614359172
```

### Perimiter

`perimiter(r)`

Returns perimiter of a circle with radius `r`

```
> perimiter(3)
18.84955592153876
```

## Square

### Area

`area(a)`

Returns area of a square with side `a`

```
> area(3)
9
```

### Perimiter

`perimiter(a)`

Returns perimiter of a square with side `a`

```
> perimiter(2)
8
```

# Tests
`class TestGeometryFunctions(unittest.TestCase)`

Returns how many tests program passed.

```
> python -m unittest tests.py
Ran 22 tests in 0.000s

OK
```

# Changelog
- `3db259a30bab855ad60f90e5a3876d70ecfeaa97` added tests, all files merged in one
- `aaccb2ef63b75faab9c6cf7aa9d3276af21fad52` Add docs and comments
- `3259b24e776F2950edb2f33f27a8af93167bc219` Fixed bag in rectangle.py
- `71b29fb058cc703a34b863d9a3F114217932a088` Add triangle.py
- `546295218a7827230a3208b465b35a8aa4075b31` Add rectangle.py
- `d078c8d9ee6155F3cb0e577d28d337b791de28e2` L-03: Docs added
- `8ba9aeb3cea847b63a91ac378a2a6db758682460` L-03: Circle and square added
