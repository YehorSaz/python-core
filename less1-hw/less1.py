# strings
#
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.

# Resolve:

# st = 'as 23 fdfdg544'
# num = ''
# for i in st:
#     if i.isdigit():
#         num += i
# print(','.join(num))


# #################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі

# Resolve:

# st = input('enter string: ')
# nums = []
# num = ''
# for i in st:
#     if i.isdigit():
#         num += i
#     else:
#         if num.isdigit():
#             nums.append(num)
#             num = ''
# if num != '':
#     nums.append(num)
# print(', '.join(nums))
# #################################################################################
#
# list comprehension
#
# 1)є строка:
# greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

# Resolve:

# greeting = 'Hello, world'
# print([i.upper() for i in greeting])
###################################################################################


# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

# Resolve:

# print([i**2 for i in range(50) if i % 2 != 0])
###################################################################################

# function
#
# - створити функцію яка виводить ліст

# Resolve:

# arr = [123, 'hello', True]
#
#
# def print_arr(some_list):
#     print(some_list)
#
#
# print_arr(arr)
###################################################################################


# - створити функцію яка приймає три числа та виводить та повертає найбільше.
# Resolve:

# def max_num(a, b, c):
#     nums = [a, b, c]
#     print(sorted(nums)[-1])
#
#
# max_num(99, 87, 45)
###################################################################################


# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
# Resolve:

# def min_max_numbers(*args: int):
#     nums = [*args]
#     return min(nums)
#
#
# min_max_numbers(3, 57, 153, 45, -3, 453, 13)
###################################################################################


# - створити функцію яка повертає найбільше число з ліста
# Resolve:

# num_list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
#
#
# def max_num(l):
#     return max(l)
#
#
# max_num(num_list)
###################################################################################


# - створити функцію яка повертає найменьше число з ліста
# Resolve:

# num_list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]

# def max_num(l):
#     return sorted(l)[0]
#
#
# max_num(num_list)
###################################################################################


# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
# Resolve:
# num_list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
#
#
# def num_sum(l):
#     return sum(l)
#
#
# print(num_sum(num_list))
###################################################################################


# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
# Resolve:
# num_list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
# def num_sum(l):
#     numbers_sum = 0
#     for i in num_list:
#         numbers_sum = numbers_sum + i
#     return numbers_sum / len(l)
#
#
# print(num_sum(num_list))


# ################################################################################################
# 1)Дан list:
#   list = [22, 3,5,2,8,2,-23, 8,23,5]
#   - знайти мін число
#   - видалити усі дублікати
#   - замінити кожне 4-те значення на 'X'
# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як аргумент функції
# 3) вивести табличку множення за допомогою циклу while
# 4) переробити це завдання під меню

# Resolve:

#
num_list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]


#

def menu():
    while True:
        choice = input(
            'Дан list: [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]\n'
            '1. - знайти мін число\n'
            '2. - видалити усі дублікати\n'
            '3. - замінити кожне 4-те значення на X\n'
            '4. -вивести на екран пустий квадрат з "*" сторона якого вказана як аргумент функції\n'
            '5. -вивести табличку множення за допомогою циклу while\n'
            'зробіть вибір: '
        )
        if choice == '1':
            print(f'мінімальне число: {sorted(num_list)[0]}')
        elif choice == '2':
            print(list(set(num_list)))
        elif choice == '3':
            for i in range(3, len(num_list), 4):
                num_list[i] = 'X'
            print(num_list)
        elif choice == '4':
            side = int(input('введіть розмір сторони: '))
            for i in range(1, side + 1):
                if i == 1 or i == side:
                    print('* ' * side)
                else:
                    print('*' + '  ' * (side - 2) + ' *')
        elif choice == '5':
            num1 = 1
            num2 = 1
            while num1 < 10:
                while num2 < 10:
                    print(f'{num1 * num2:2}', end=' ')
                    num2 += 1
                print()
                num1 += 1
                num2 = 1
        elif choice == '9':
            break


menu()
