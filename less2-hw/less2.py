# 1)написати функцію на замикання котра буде в собі зберігати список справ,
# вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи


# from typing import Callable
#
#
# def notebook() -> list[Callable[[str], list[str]] | Callable[[], list[str]]]:
#     todo_list = []
#
#     def add_todo(todo: str) -> list[str]:
#         todo_list.append(todo)
#         return todo_list
#
#     def get_all() -> list[str]:
#         print(*todo_list, sep="\n")
#         return todo_list
#
#     return [add_todo, get_all]
#
#
# add_todo, get_all = notebook()
# add_todo('first')
# add_todo('second')
# get_all()

####################################################################################

# створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)

# number = int(input('enter number: '))


# def digit(num: int) -> list[int]:
#     res = []
#     num = str(num)
#     divider = int('1' + ('0' * (len(num) - 1)))
#
#     res.append(int(num) - int(num) % divider)
#     for n in range(len(num) - 1):
#         n = int(num) % divider
#         divider /= 10
#         if divider == 0:
#             break
#         if n - n % divider != 0:
#             res.append(int(n - n % divider))
#
#     print(*res, sep=" + ")
#     return res
#
#
# digit(number)

##############################################################################

# створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим декоратором,
# та буде виводити це значення після виконання функці

# def decor(fn):
#     count = 0
#
#     def inner(*args, **kwargs):
#         nonlocal count
#         count += 1
#         print(f'count: {count}')
#         fn(*args, **kwargs)
#         print('---------------------')
#
#     return inner
#
#
# @decor
# def funk1():
#     print('fn1')
#
#
# @decor
# def funk2():
#     print('fn2')
#
#
# funk1()
# funk1()
# funk1()
#
# funk2()
# funk2()
