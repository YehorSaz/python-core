# Створити клас Rectangle:
# -він має приймати дві сторони x,y
# -описати поведінку на арифметични методи:
#   + сумма площин двох екземплярів ксласу
#   - різниця площин двох екземплярів ксласу
#   == площин на рівність
#   != площин на не рівність
#   >, < меньше більше
#   при виклику метода len() підраховувати сумму сторін


# class Rectangle:
#
#     def __init__(self, x, y):
#         self.y = y
#         self.x = x
#
#     def __add__(self, other):
#         return (self.x * self.y) + (other.x * other.y)
#
#     def __sub__(self, other):
#         return (self.x * self.y) - (other.x * other.y)
#
#     def __eq__(self, other):
#         return (self.x * self.y) == (other.x * other.y)
#
#     def __ne__(self, other):
#         return (self.x * self.y) != (other.x * other.y)
#
#     def __lt__(self, other):
#         return (self.x * self.y) < (other.x * other.y)
#
#     def __gt__(self, other):
#         return (self.x * self.y) > (other.x * other.y)
#
#     def __len__(self):
#         return self.x + self.y
#
#
# rec1 = Rectangle(20, 30)
# rec2 = Rectangle(20, 40)
#
# print(rec1 + rec2)
# print(rec1 == rec2)
# print(rec1 != rec2)
# print(len(rec2))
#################################################################

# створити класс Human (name, age)
# створити два класси Prince и Cinderella які наслідуються від Human:
# у попелюшки мае бути ім'я, вік, розмір нонги
# у принца має бути ім'я, вік, та розмір знайденого черевичка,
# а також метод котрий буде приймати список попелюшок, та шукати ту саму

# в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
# також має бути метод классу який буде виводити це значення

#-------------------------------------------------------------------
# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# class Cinderella(Human):
#     __count = 0
#
#     def __init__(self, name, age, foot_size):
#         super().__init__(name, age)
#         self.foot_size = foot_size
#         Cinderella.__count += 1
#
#     @classmethod
#     def get_count(cls):
#         print(cls.__count)
#
#
# class Prince(Human):
#     def __init__(self, name, age, shoe_size):
#         super().__init__(name, age)
#         self.shoe_size = shoe_size
#
#     def find_cinderella(self, cinderellas: list[Cinderella]):
#         for cinderella in cinderellas:
#             if self.shoe_size == cinderella.foot_size:
#                 print(cinderella.__dict__)
#                 return
#         print('Not found!!!')
#
#
# cinderellas = [
#     Cinderella('Olha', 20, 35),
#     Cinderella('Kamila', 30, 36),
#     Cinderella('Marina', 20, 32),
#     Cinderella('Albina', 20, 45),
# ]
#---------------------------------------------------------------------


# class Human:
#     cinderellas = []
#
#     def __init__(self, name, age):
#         self.age = age
#         self.name = name
#
#
# class Prince(Human):
#     __instance = None
#
#     def __new__(cls, *args, **kwargs):
#
#         if not isinstance(cls.__instance, cls):
#             cls.__instance = super().__new__(cls)
#
#         return cls.__instance
#
#     def __init__(self, name, age, size):
#         super().__init__(name, age)
#         self.size = size
#
#     def find_cinderella(self):
#         for i in Human.cinderellas:
#             if i.foot_size == self.size:
#                 print(i.name)
#
#
# class Cinderella(Human):
#     count = 0
#
#     def __init__(self, name, age, foot_size):
#         super().__init__(name, age)
#         self.foot_size = foot_size
#         Cinderella.count += 1
#         Human.cinderellas.append(self)
#
#     @classmethod
#     def get_count(cls):
#         print(Cinderella.count)
#
#
# prince = Prince('Ivan', 30, 37)
#
# cin1 = Cinderella('Anna', 23, 38)
# cin2 = Cinderella('Marina', 18, 37)
# cin3 = Cinderella('Kristina', 20, 36)
# cin4 = Cinderella('Masha', 24, 35)
#
# prince.find_cinderella()
# Cinderella.get_count()
###############################################################################

# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()

# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name,
# та який наслідуются від класу Printable
# 3) Створити клас Main в якому буде:
# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додавати екземпляри класів в список
# і робити перевірку чи то що передають є класом Book або Magazine инакше ігрнорувати додавання
# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного класу
# - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу


# from abc import ABC, abstractmethod
#
#
# class Printable(ABC):
#     def __init__(self, name):
#         self.name = name
#
#     @abstractmethod
#     def print(self):
#         pass
#
#
# class Book(Printable):
#
#     def print(self):
#         print(f'Book: {self.name}')
#
#
# class Magazine(Printable):
#
#     def print(self):
#         print(f'Magazine: {self.name}')
#
#
# class Main(Printable, ABC):
#     __printable_list: list[Printable] = []
#
#     @classmethod
#     def add(cls, item: Printable):
#         if isinstance(item, Printable):
#             cls.__printable_list.append(item)
#         else:
#             print('Ignored...')
#
#     @classmethod
#     def show_all_magazines(cls):
#         for item in cls.__printable_list:
#             if isinstance(item, Book):
#                 item.print()
#
#     @classmethod
#     def show_all_books(cls):
#         for item in cls.__printable_list:
#             if isinstance(item, Magazine):
#                 item.print()
#
#
# class SomeClass:
#     pass
#
#
# Main.add(SomeClass())
#
# Main.add(Book('book1'))
# Main.add(Book('book2'))
# Main.add(Magazine('Magazine1'))
# Main.add(Magazine('Magazine2'))
#
# Main.show_all_magazines()
# print('-' * 50)
# Main.show_all_books()
