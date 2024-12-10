import math

def circleArea(r):
    '''Принимает 1 значение r. r - радиус окружности. Возвращает площадь окружности.'''
    if not isinstance(r, (int, float)):
        raise TypeError("Радиус должен быть числом.")
    if r < 0:
        raise ValueError("Радиус не может быть отрицательным.")
    return math.pi * r * r

def circlePerimeter(r):
    '''Принимает 1 значение r. r - радиус окружности. Возвращает периметр окружности.'''
    if not isinstance(r, (int, float)):
        raise TypeError("Радиус должен быть числом.")
    if r < 0:
        raise ValueError("Радиус не может быть отрицательным.")
    return math.pi * r * 2

def rectangleArea(a, b):
    '''Принимает 2 числа, a и b. a - первая сторона прямоугольника, b - вторая сторона прямоугольника. Возвращает площадь прямоугольника.'''
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Стороны должны быть числами.")
    if a < 0 or b < 0:
        raise ValueError("Стороны не могут быть отрицательными.")
    return a * b

def rectanglePerimeter(a, b):
    '''Принимает 2 числа a и b. a - первая сторона прямоугольника, b - вторая сторона прямоугольника. Возвращает периметр прямоугольника.'''
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Стороны должны быть числами.")
    if a < 0 or b < 0:
        raise ValueError("Стороны не могут быть отрицательными.")
    return (a + b) * 2

def squareArea(a):
    '''Принимает 1 значение а. а - сторона квадрата. Возвращает площадь квадрата.'''
    if not isinstance(a, (int, float)):
        raise TypeError("Сторона должна быть числом.")
    if a < 0:
        raise ValueError("Сторона не может быть отрицательной.")
    return a * a

def squarePerimeter(a):
    '''Принимает 1 значение а. а - сторона квадрата. Возвращает периметр квадрата.'''
    if not isinstance(a, (int, float)):
        raise TypeError("Сторона должна быть числом.")
    if a < 0:
        raise ValueError("Сторона не может быть отрицательной.")
    return 4 * a

def traingleArea(a, h):
    '''Принимает 2 значения, a и h. a - сторона треугольника, h - высота, проведенная к стороне a. Возвращает площадь треугольника.'''
    if not isinstance(a, (int, float)) or not isinstance(h, (int, float)):
        raise TypeError("Сторона и высота должны быть числами.")
    if a < 0 or h < 0:
        raise ValueError("Сторона и высота не могут быть отрицательными.")
    return a * h / 2

def trainglePerimeter(a, b, c):
    '''Принимает 3 значения, a, b и c. a - первая сторона треугольника, b - вторая сторона треугольника, c - третья сторона треугольника. Возвращает периметр треугольника.'''
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        raise TypeError("Все стороны должны быть числами.")
    if a < 0 or b < 0 or c < 0:
        raise ValueError("Стороны не могут быть отрицательными.")
    return a + b + c
