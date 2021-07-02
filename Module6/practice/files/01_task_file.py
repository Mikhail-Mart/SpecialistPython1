# Дан файл data/limericks.txt с лимериками(короткими стихотворениями)

# 1. Выведите содержимое файла в консоль
# 2. Узнайте количество непробельный символов в данном файле
# 3. Узнайте количество стихотворений, если известно,
# что каждое стихотворение отделяется пустой строкой от предыдущего

with open('data/limericks.txt', 'r', encoding='utf-8') as f:
    summ=0
    for my_line in f:
        my_line = my_line.rstrip()
        summ += len(my_line.replace(' ',''))



print(summ)

with open('data/limericks.txt', 'r', encoding='utf-8') as f:
    summ=0
    my_len_prev = 0
    for my_line in f:
        my_line = my_line.rstrip()
        my_len = len(my_line)

        if my_len > 0 and my_len_prev == 0:
            summ += 1
        my_len_prev = my_len


print(summ)
