def classify_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError('side <= 0')
    else:
        if a == b or b == c or c == a:
            if a == b and b == c:
                return 'equilateral triangle'
            else:
                return 'isosceles triangle'
        elif round(((a ** 2) + (b ** 2)), 2) == round((c ** 2), 2):
            return 'right triangle'
        elif a + b > c or a + c > b or b + c > a:
            return 'scalene triangle'
        else:
            return 'it is not a triangle'
