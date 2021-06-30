# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# TODO: your code here

import random

numbers = []

n = 5
for i in range(n):
    numbers.append(random.randint(0, 200) - 100)
#print(numbers)
sum = 0
for el in numbers:
    if el > 0 and el % 2 == 0:
        sum += el
print(sum)
