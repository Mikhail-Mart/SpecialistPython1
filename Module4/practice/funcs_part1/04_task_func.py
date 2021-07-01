# Даны координаты трех точек p1(x1; y1) p2(x2; y2) p3(x3; y3).
# Напишите функцию, проверябщую можно ли построить треугольник, соединив данные точки отрезками




def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def can_triangle(p1, p2, p3):
    # TODO: your code here
    my_line_a = distance(p1[0], p1[1], p2[0], p2[1])
    my_line_b = distance(p2[0], p2[1], p3[0], p3[1])
    my_line_c = distance(p1[0], p1[1], p3[0], p3[1])
    return my_line_a + my_line_b > my_line_c


# Пример вызова функции
#can_triangle((10, 12), (14, 18), (12, 12))

p1 = 10, 12
p2 = 14, 18
p3 = 12, 12

#p1 = 10, 10
#p2 = 11, 11
#p3 = 12, 12



if can_triangle( p1, p2, p3):
    print("существует")
else:
    print("не существует")
