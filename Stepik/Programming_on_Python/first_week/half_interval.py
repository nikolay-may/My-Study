# Напишите программу, принимающую на вход целое число, которая выводит True, если переданное значение попадает 
# в интервал (-15, 12] \cup (14, 17) \cup [19, +\infty)(−15,12]∪(14,17)∪[19,+∞) и False в противном случае (регистр символов имеет значение).

# Обратите внимание на разные скобки, используемые для обозначения интервалов. В задании используются полуоткрытые и открытые интервалы. 
# Подробнее про это вы можете прочитать, например, на википедии (полуинтервал, промежуток).

#  №1
X = int(input())
if X<=12 and X>-15:
    print('True')
elif X>14 and X<17:
    print('True')
elif X>=19:
    print('True')
else:
    print('False')


# №2
x = int(input("Ведите число: "))
def half_interval(x):
    if (X <= 12 and X > -15) or (X > 14 and X < 17) or (X >= 19):
        return True
    else:
        return False

print(half_interval(X))
