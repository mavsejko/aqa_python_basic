from math import sqrt, pow
import random
import time
import requests
import my_module
from utils import greet
import matplotlib.pyplot as plt
import math_operations
"""
++++++++++++++++++++++++++++++++++++++++++++++++
Модули в Python
++++++++++++++++++++++++++++++++++++++++++++++++
===============================================
1. Импортируйте только функции sqrt и pow из модуля math_operations и вычислите:
Квадратный корень из 64
5 в степени 3
Ожидаемый вывод:
8.0
125.0
===============================================
"""

print(sqrt(64))
print(pow(5, 3))

"""
2. Импортируйте модуль random и:
Выведите случайное число от 1 до 10
Выберите случайный элемент из списка [Python, Java, C++]
Ожидаемый вывод:
Случайное число: 7  # (значение может отличаться)
Выбранный язык: Python  # (значение может отличаться)
===============================================
"""

print(f"Случайное число: {random.randint(1, 10)}")
print(f"Выбранный язык: {random.choice(['Python', 'Java', 'C++'])}")

"""
3. Создайте свой модуль my_module.py, в котором будут функции:
add(a, b): складывает два числа
multiply(a, b): умножает два числа
Пример вызова в другом файле:
import my_module

print(my_module.add(3, 5))  # 8
print(my_module.multiply(4, 6))  # 24
Cоздайте my_module.py в той же папке!
===============================================
"""

print(my_module.add(3, 5))  # 8
print(my_module.multiply(4, 6))  # 24

"""
4. Создайте два Python-файла:

utils.py – в нем создайте функцию greet(name), которая выводит приветствие.
main.py – в нем импортируйте greet() из utils.py и вызовите её.
Пример вызова в main.py
from utils import greet

greet("Алексей")  # Привет, Алексей!
Запустите main.py и убедитесь, что импорт работает!
===============================================
"""

greet("Алексей")

"""
5. Напишите программу, которая измеряет время выполнения кода с помощью time.sleep(2), используя модуль time.
Ожидаемый вывод:
Код выполнялся 2.0001 сек
===============================================
"""

st_time = time.time()
time.sleep(2)
res = time.time() - st_time
print(res)

"""
6. Установите библиотеку requests и проверьте, работает ли она.
Напишите код, который делает HTTP-запрос и получает данные с сайта:
import requests

response = requests.get("https://api.github.com")
print(response.status_code)  # Должно вывести 200
===============================================
"""

response = requests.get("https://api.github.com")
print(response.status_code)

"""
7. Установите библиотеку matplotlib и постройте график.
Напишите код:
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 50]

plt.plot(x, y, marker='o')
plt.title("Пример графика")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
===============================================
"""

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 50]

plt.plot(x, y, marker='o')
plt.title("Пример графика")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

"""
8. Создайте requirements.txt с зависимостями вашего проекта.
Удалите один из установленных модулей, например requests
Восстановите зависимости с помощью установки из requirements.txt
===============================================
9. Создание простого пакета
Создайте пакет math_operations с модулями:
addition.py → Функция add(a, b) складывает 2 числа
subtraction.py → Функция subtract(a, b) вычитает
Структура проекта:

math_operations/
│── __init__.py
│── addition.py
│── subtraction.py
main.py

И запустите обе функции в main.py
"""
print(math_operations.add(5, 6))
print(math_operations.subtraction(5, 2))


