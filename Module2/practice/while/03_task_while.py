# По данному натуральному n выведите лесенку из n ступенек, i-я ступень состоит из чисел от 1 до i без пробелов.
# Формат входных данных: Вводится натуральное число n.
# Формат выходных данных: Выведите ответ на задачу.
# Пример:
# Для n = 4
# Нужно вывести:
# 1
# 12
# 123
# 1234

# TODO: your code here

x = 1
y = 1
number = int(input("введите число "))

while x <= number:
    print(y)
    x += 1
    y = y*10 + x
