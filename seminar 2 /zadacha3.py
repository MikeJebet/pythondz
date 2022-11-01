n = int(input('Введите число n: '))
sum = 0
list = []
for i in range(1, n + 1):
    a = round(((1 + 1 / i) ** i), 2)
    list.append(a)
    sum = sum + a

print(list)
print('Сумма элементов списка: ', sum)