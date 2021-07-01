# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.

a = 100
b = 1000

def find_palindrome(a, b):
    summa = 0
    for num in range(a, b):
        if palindrome(num):
            summa += 1
    return summa
