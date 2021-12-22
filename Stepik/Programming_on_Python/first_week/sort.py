# Напишите программу, которая получает на вход три целых числа, по одному числу в строке, 
# и выводит на консоль в три строки сначала максимальное, потом минимальное, после чего оставшееся число.
# На ввод могут подаваться и повторяющиеся числа.

# №1
a = int(input())
b = int(input())
c = int(input())
d = list(sorted([a,b,c]))

print (d[-1])
print (d[0])
print (d[1])

# №2
a,b,c = int(input()),int(input()),int(input())
maxim = a
minim = b
if b > a:
    maxim = b
    minim = a
if c > maxim:
    maxim = c
if c < minim:
    minim = c
ost = a + b + c - minim - maxim
print(maxim)
print(minim)
print(ost)

# №3

def sort(a, b, c ):
    if a <= b:
        a, b = b, a
    if b <= c:
        b, c = c, b
    if a <= b:
        a, b = b, a
    return a, c, b

a, b, c = int(input()), int(input()), int(input())

print(sort(a,b,c))