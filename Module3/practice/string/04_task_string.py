# Дана строка текста, слова разделены пробелами, знаки препинания отсутствуют.
# Определить в предоставленном сообщении количество слов длиной больше, чем 5.

text = "Lorem ipsum dolor sit amet consectetur adipiscing elit Integer porttitor bibendum nisi ut convallis ante"
# Примечание: для генериации текста можете воспользоваться сайтом: https://ru.lipsum.com/

# TODO: your code here
x = 0
sum = 0
lengh_text = len(text)
while x <= lengh_text:
    y = text.find(" ", x)
    print("len x", x, y)
    if y == -1:
        y = lengh_text
    elif y-x>5:
        sum += 1
    x = y+1
print("количество слов", sum)
