# Дан список имен.
# Выведите все имена в одну строку через запятую

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

# TODO: your code here

# Пример вывода:
# Иван, Ирина, Вячеслав, Василий, Петр

str = ""
ln = len(names)
for name in names:
    str += (name)
    if  names[ln-1] != name:
        str += ("," + " ")
print(str)
