# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

n = int(input('Введите номер четверти от 1 до 4: '))
if n == 1:
    print('x > 0, y > 0')
if n == 2:
    print('x < 0, y > 0')
if n == 3:
    print('x < 0, y < 0')
if n == 4:
    print('x > 0, y < 0')
if n > 4 or n <= 0:
    print('Ошибка ввода!')