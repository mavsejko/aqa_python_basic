"""
++++++++++++++++++++++++++++++++++++++++++++++++
Лямбда-функции
++++++++++++++++++++++++++++++++++++++++++++++++
===============================================
1. Создайте lambda-функцию, которая возвращает квадрат числа.
===============================================
"""

square = lambda x: x ** 2

"""
2. Создайте lambda-функцию, которая проверяет, является ли число четным.
===============================================
"""

is_even = lambda x: x % 2 == 0

"""
3. Используйте lambda в sorted(), чтобы отсортировать список строк по последней букве.
Пример вызова:
words = ["banana", "apple", "cherry"]
print(sort_by_last_letter(words))
Ожидаемый результат:
['banana', 'apple', 'cherry']
===============================================
"""

words = ["banana", "apple", "cherry"]


def sort_by_last_letter(lst):
    return sorted(lst, key=lambda x: x[-1])


print(sort_by_last_letter(words))

"""
++++++++++++++++++++++++++++++++++++++++++++++++
Замыкания
++++++++++++++++++++++++++++++++++++++++++++++++
1. Создайте функцию multiply_by(n), которая принимает число n и возвращает вложенную функцию.
Вложенная функция должна принимать число x и возвращать его произведение на n.
Пример вызова:
times3 = multiply_by(3)
times5 = multiply_by(5)

print(times3(10))  # 30
print(times5(10))  # 50
++++++++++++++++++++++++++++++++++++++++++++++++
"""


def multiply_by(n):
    def func_inner(x):
        return x * n
    return func_inner


times3 = multiply_by(3)
times5 = multiply_by(5)

print(times3(10))  # 30
print(times5(10))  # 50

"""
2. Напишите функцию counter(start=0), которая возвращает вложенную функцию.
Каждый вызов вложенной функции должен увеличивать счетчик на 1.
Пример вызова:

c1 = counter(5)
c2 = counter()

print(c1())  # 6
print(c1())  # 7
print(c2())  # 1
print(c2())  # 2

Подсказка: используйте nonlocal
"""


def counter(start=0):
    count = start

    def increment():
        nonlocal count
        count += 1
        return count
    return increment


c1 = counter(5)
c2 = counter()

print(c1())  # 6
print(c1())  # 7
print(c2())  # 1
print(c2())  # 2
