# Дана строка текста, слова разделены пробелами.
# В предложении могут присутствовать следующие знаки препинания ",.!?-". Знаки препинания частьюслова не являются.
# Определить в предоставленном сообщении количество слов длиной больше, чем 7.

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam placerat consequat vestibulum. " \
       "Donec tincidunt sed lorem et feugiat. Nullam elementum"
# Примечание: для генериации текста можете воспользоваться сайтом: https://ru.lipsum.com/
# Примечание: обратите внимание на перенос длинной строки на новую строку

# TODO: your code here

text = text.replace(',','')
text = text.replace('.','')
text = text.replace('!','')
text = text.replace('?','')
text = text.replace('-','')


x = 0
sum = 0
lengh_text = len(text)
while x <= lengh_text:
    y = text.find(" ", x)
    print("len x", x, y)
    if y == -1:
        y = lengh_text
    elif y-x > 7:
        sum += 1
    x = y+1
print("количество слов", sum)
