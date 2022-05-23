# 1 - Написать функцию, которая принимает на вход два аргумента.
# Если аргументы больше нуля, возвращаем их сумму. Если оба меньше - разность. Если знаки разные - возвращаем 0.

def math_operation(a, b):
    if a > 0 and b > 0:
        return a + b
    elif a < 0 and b < 0:
        return a - b
    else:
        return 0

print(math_operation(15, 10))
print(math_operation(-5, -10))
print(math_operation(10, -10))

# 2 - Написать функцию, которая принимает 3 аргумента - числа, найти среди них два максимальных, вывести в консоль.

def max_number(a, b, c):
    lst = []
    for i in a, b, c:
        lst.append(i)
    lst.remove(min(lst)) 
    print(lst)

max_number(13.2, 13.3, 15)

# 3 - Написать функцию, которая принимает два аргумента. Первый - список чисел, второй - булевый флаг. 
# Если флаг действителен - возвращаем новый список с нечетными числами из входного списка, если флаг отрицателен - возвращаем новый список с четными числами из входного списка.

a = [3, 4, 77, 89, 6, 20]
b = True

def even_odd_nmbrs(a, b):
    even_lst = []
    odd_lst = []
    if b:
        for number in a:
            if number % 2 != 0:
               even_lst.append(number)
        return even_lst
    else:
        for number in a:
            if number % 2 == 0:
               odd_lst.append(number)
        return odd_lst

print(even_odd_nmbrs(a, b))

# 4 - Написать функцию, которая принимает любое количество аргументов чисел. Среди них она находит максимальное и минимальное. 
# И возвращает оба.

def min_max_nmbrs(*args):
    return min(args), max(args)

# 5 - Написать функцию, которая принимает два аргумента: строка и булевый флаг case по-умолчанию равный True. 
# Если флаг действителен: возвращаем новую строку, где каждый символ входной приведен к верхнему регистру, иначе - к нижнему.

def upperLowerCase(a, b=True):
    if b == True:
        up = a.upper()
        return up
    else:
        low = a.lower()
        return low

print(upperLowerCase('Hello World', b=False))

# 6 -Написать функцию, которая принимает любое количество позиционных аргументов - строк и один парматер по-умолчанию glue, который равен ':'. Соединить все строки таким образом, чтобы в результат попали все строки, длинее 3 символов. 
# Для соединения между любых двух строк вставлять glue.

def str_glue(*args, glue = ':'):
    lst = []
    for i in args:
        if len(i) > 3:
            lst.append(i)
    return glue.join(lst)

print(str_glue('Москва', 'Рим', 'Осло', 'Барселона', 'Ош', 'Ташкент', 'Будапешт'))
