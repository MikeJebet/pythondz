# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number = int(input('Введите число: '))
list = []

for i in range(1, number + 1):
    list.append(i)

print(list)

for i in range(1, number):
    list[i] = list[i] * list[i - 1]

print('Итоговый список:', list)
