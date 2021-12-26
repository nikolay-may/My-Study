# Паша очень любит кататься на общественном транспорте, а получая билет, сразу проверяет, счастливый ли ему попался. 
# Билет считается счастливым, если сумма первых трех цифр совпадает с суммой последних трех цифр номера билета.

# Однако Паша очень плохо считает в уме, поэтому попросил вас написать программу, 
# которая проверит равенство сумм и выведет "Счастливый", если суммы совпадают, и "Обычный", если суммы различны.

# На вход программе подаётся строка из шести цифр.

# Выводить нужно только слово "Счастливый" или "Обычный", с большой буквы.


# №1
h = str(input())
a =int(h[0])
b = int(h[1])
c = int(h[2])
d = int(h[3])
e = int(h[4])
f = int(h[5])
abc = a + b +c
d_ef = d + e + f
if abc == d_ef:
    print("Счастливый")
elif abc != d_ef:
    print("Обычный")



# №2

def happy_ticket(s):
    first_half = int(s[0]) +int(s[1]) + int(s[2])
    second_half = int(s[3]) +int(s[4]) +int(s[5])
    if first_half == second_half:
        return 'Счастливый'
    else:
        return 'Обычный'

print(happy_ticket(input()))