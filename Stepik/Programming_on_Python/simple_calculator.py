# Напишите простой калькулятор, который считывает с пользовательского ввода три строки: первое число, второе число и операцию,
#  после чего применяет операцию к введённым числам ("первое число" "операция" "второе число") и выводит результат на экран.

# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.

# Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".

# Обратите внимание, что на вход программе приходят вещественные числа.

# №1
A = float (input())
B = float (input())
C = input()
if C =='+':
    print(A+B)
elif C=='-':
    print(A-B)
elif C=='*':
    print(A*B)
elif C=='/' and B==0:
    print("Деление на 0!")
elif C=='/' and B!=0:
    print(A/B)
elif C=='mod' and B==0:
    print('Деление на 0!')
elif C=='mod' and B!=0:
    print(A%B)
elif C=='pow':
    print(A**B)
elif C=='div' and B==0:
    print('Деление на 0!')
elif C=='div' and B!=0:
    print(A//B)


# №2
num_1, num_2, action = float(input("Введите первую цифру: ")), float(input("Введите фторую цифру: ")), input("Введите знак операции: ")

def simple_calculator(num_1, num_2, action):
    if (action == '/' and num_2 == 0) or (action == 'mod' and num_2 == 0) or (action == 'div' and num_2 == 0):
        return "Деление на 0 !"
    elif action == '+':
        return num_1 + num_2
    elif action == '-':
        return num_1 - num_2
    elif action == '/' and num_2 != 0:
        return num_1 / num_2
    elif action == 'mod' and num_2 != 0:
        return num_1 % num_2
    elif action == 'div' and num_2 != 0:
        return num_1 // num_2
    elif action == '*':
        return num_1 * num_2
    elif action == '**':
        return num_1 ** num_2

print(simple_calculator(num_1, num_2, action))

        
