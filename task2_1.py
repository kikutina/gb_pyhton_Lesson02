# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = [25, 56.76, True, None, "Hi", [1,2], (3, 4), {5, 6}, {'key_1' : 25}]
for i in my_list:
    print(f'{i} is {type(i)}')

