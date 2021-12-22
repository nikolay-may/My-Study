# Жители страны Малевии часто экспериментируют с планировкой комнат. Комнаты бывают треугольные, 
# прямоугольные и круглые. Чтобы быстро вычислять жилплощадь, требуется написать программу, на вход которой 
# подаётся тип фигуры комнаты и соответствующие параметры, которая бы выводила площадь получившейся комнаты.
# Для числа π в стране Малевии используют значение 3.14.

# №1
import math
t = str (input())
if t =='треугольник':
    a = int (input())
    b = int (input())
    c = int (input())
    p = (a+b+c)/2
    S = math.sqrt(p * (p-a) * (p-b) * (p-c))
    print(S)
elif t =='прямоугольник':
    a = int (input())
    b = int (input())
    S = a * b
    print(S)
elif t =='круг':
    r = int (input())
    S = 3.14 * r**2
    print(S)

# №2

P = 3,14
room = input()

def malivis_room(room):
    if room == "треугольник":
        a, b, c = int(input("Введите цифру: ")), int(input("Введите цифру: ")), int(input("Введите цифру: "))
        p = (a + b + c) / 2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5
        
    elif room == "прямоугольник":
        a, b = int(input("Введите цифру: ")), int(input("Введите цифру: "))
        return a * b
    elif room == "круг":
        r = int(input("Введите цифру: "))
        return P * r ** 2

print(malivis_room(room))




