import math
figures = input()
if figures == 'square':
    a = float(input())
    square = a * a
    print(f'{square:.3f}')
if figures == 'rectangle':
    a = float(input())
    height = float(input())
    rectangle = a * height
    print(f'{rectangle:.3f}')
if figures == 'circle':
    radius = float(input())
    circle = math.pi * (radius * radius)
    print(f'{circle:.3f}')
if figures == 'triangle':
    a = float(input())
    height = float(input())
    triangle = (height * a) / 2
    print(f'{triangle:.3f}')