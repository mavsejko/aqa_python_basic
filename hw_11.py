"""
++++++++++++++++++++++++++++++++++++++++++++++++
Функции в Python
++++++++++++++++++++++++++++++++++++++++++++++++
===============================================
1. Привет, <name>! Добро пожаловать!
Пример вызова:
greet("Анна")
Ожидаемый результат:
Привет, Анна! Добро пожаловать!
===============================================
"""


def greet(name):
    print(f"Привет, {name}! Добро пожаловать!")


greet("Анна")

"""
2. Напишите функцию square(num), которая принимает число и возвращает его квадрат.
Пример вызова:
print(square(5))
Ожидаемый результат:
25
===============================================
"""


def square(num):
    return num ** 2


print(square(5))

"""
3. Создайте функцию is_even(num), которая возвращает True, если число четное, и False, если нечетное.
Пример вызова:
print(is_even(4))
print(is_even(7))
Ожидаемый результат:
True
False
===============================================
"""


def is_even(num):
    return num % 2 == 0


print(is_even(4))
print(is_even(7))

"""
4. Напишите функцию repeat_string(text, times), которая повторяет строку text times раз.
Пример вызова:
print(repeat_string("Python", 3))
Ожидаемый результат:
PythonPythonPython
===============================================
"""


def repeat_string(text, times):
    return text*times


print(repeat_string("Python", 3))

"""
5. Напишите функцию add(a, b), которая принимает два числа и возвращает их сумму.
Пример вызова:
print(add(3, 7))
Ожидаемый результат:
10
===============================================
"""


def add(a, b):
    return a + b


print(add(3, 7))

"""
6. Напишите функцию get_max(a, b, c), которая возвращает максимальное из трех чисел.
Пример вызова:
print(get_max(10, 25, 7))
Ожидаемый результат:
25
===============================================
"""


def get_max(a, b, c):
    return max(a, b, c)


print(get_max(10, 25, 7))

"""
7. Создайте функцию calculate(a, b, operation), которая выполняет одну из операций:
"+" — сложение
"-" — вычитание
"*" — умножение
"/" — деление
Пример вызова:
print(calculate(10, 5, "+"))
print(calculate(10, 5, "*"))
Ожидаемый результат:
15
50
===============================================
"""


def calculate(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b == 0:
            return "ZeroDivError"
        return a / b


print(calculate(10, 5, "+"))
print(calculate(10, 5, "*"))

"""
8. Создайте функцию reverse_string(text), которая принимает строку и возвращает её в обратном порядке.
Пример вызова:
print(reverse_string("Python"))
Ожидаемый результат:
nohtyP
===============================================
"""


def reverse_string(text):
    return text[::-1]


print(reverse_string("Python"))

"""
9. Создайте функцию compare_strings(s1, s2, ignore_case=True, ignore_spaces=True),
которая сравнивает две строки, убирая пробелы и регистр, если соответствующие параметры установлены в True.
Пример вызова:
print(compare_strings("Hello", " hello "))  # True
print(compare_strings("Hello", "HELLO", ignore_case=False))  # False
print(compare_strings("Hello ", "Hello", ignore_spaces=False))  # False
===============================================
"""


def compare_strings(s1, s2, ignore_case=True, ignore_spaces=True):
    if ignore_case:
        s1 = s1.upper()
        s2 = s2.upper()
    if ignore_spaces:
        s1 = s1.replace(" ", "")
        s2 = s2.replace(" ", "")
    return s1 == s2


print(compare_strings("Hello", " hello "))  # True
print(compare_strings("Hello", "HELLO", ignore_case=False))  # False
print(compare_strings("Hello ", "Hello", ignore_spaces=False))  # False

"""
10. Напишите функцию summarize(*args), которая возвращает сумму всех переданных чисел.
Если переданы нечисловые значения, игнорируйте их.
Пример вызова:
print(summarize(1, 2, 3))           # 6
print(summarize(10, "abc", 5, 2))   # 17 (игнорируем "abc")
===============================================
"""


def summarize(*args):
        return sum([i for i in args if isinstance(i, (int, float)) and not isinstance(i, bool)])


print(summarize(1, 2, 3))           # 6
print(summarize(10, "abc", 5, 2))   # 17 (игнорируем "abc")

"""
11. Напишите функцию create_profile(name, age, **extra),
которая принимает имя, возраст и дополнительные параметры
(например, city, job, hobby) и выводит информацию о пользователе.
Пример вызова:
create_profile("Иван", 30, city="Москва", job="Инженер")
Ожидаемый результат:
Профиль пользователя:
Имя: Иван
Возраст: 30
Дополнительная информация:
city: Москва
job: Инженер
===============================================
"""


def create_profile(name, age, **extra):

    print(f"Имя: {name}\nВозраст: {age}\nДополнительная информация:")
    for key, value in extra.items():
        print(f"{key}: {value}")


create_profile("Иван", 30, city="Москва", job="Инженер")

"""
12. Напишите функцию process_orders(*orders, discount=0),
которая принимает список заказов (чисел) и применяет скидку.
Пример вызова:
print(process_orders(100, 200, 300, discount=10))
Ожидаемый результат:
Сумма заказа: 600
С учетом скидки: 540
===============================================
"""


def process_orders(*orders, discount=0):
    sum_orders = sum(orders)
    res = f"Ожидаемый результат:\nСумма заказа: {sum_orders}\nС учетом скидки: {sum_orders*(1-discount/100)}"
    return res


print(process_orders(100, 200, 300, discount=10))

"""
13. Создайте функцию merge_lists(*lists), которая объединяет несколько списков в один.
Пример вызова:
print(merge_lists([1, 2], [3, 4], [5, 6]))
Ожидаемый результат:
[1, 2, 3, 4, 5, 6]
===============================================
"""


def merge_lists(*lists):
    res = []
    for l in lists:
        res.extend(l)
    return res


print(merge_lists([1, 2], [3, 4], [5, 6]))

"""
14. Создайте функцию merge_dicts(*dicts), которая объединяет несколько словарей в один.
При совпадении ключей используется последнее значение.
Пример вызова:
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d3 = {"c": 5, "d": 6}
print(merge_dicts(d1, d2, d3))
Ожидаемый результат:
{'a': 1, 'b': 3, 'c': 5, 'd': 6}
"""


def merge_dicts(*dicts):
    res = {}
    for d in dicts:
        res.update(d)
    return res


d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d3 = {"c": 5, "d": 6}
print(merge_dicts(d1, d2, d3))


