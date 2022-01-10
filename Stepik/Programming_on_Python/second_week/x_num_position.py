# Напишите программу, которая считывает список чисел lstlst из первой строки и число xx из второй строки, 
# которая выводит все позиции, на которых встречается число xx в переданном списке lstlst.
# Позиции нумеруются с нуля, если число xx не встречается в списке, вывести строку "Отсутствует" (без кавычек, с большой буквы).
# Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.

# №1
lst = [int(i) for i in input().split()]
x = int(input())
if x not in lst:
     print('Отсутствует')
else:
     for i in range(0,len(lst)):
         if lst[i] == x:
             print(i,end=' ')



# №2
def x_num_position(lst):
    x_position =[]
    x = int(input())
    if x not in lst:
        print('Отсутствует')
    else:
        for i in range(0, len(lst)):
            if lst[i] == x:
                x_position.append(i)
        return x_position

                
lst = [int(i) for i in input().split()]
print(x_num_position(lst))