import time
"""
++++++++++++++++++++++++++++++++++++++++++++++++
Декораторы в Python
++++++++++++++++++++++++++++++++++++++++++++++++
===============================================
1. Напишите декоратор uppercase_decorator, который делает результат выполнения функции прописными буквами.
Пример вызова:
@uppercase_decorator
def say_hello():
    return "hello, world!"
print(say_hello())  # "HELLO, WORLD!"
===============================================
"""


def uppercase_decorator(func):
    def wrapper():
        text = func()
        return text.upper()

    return wrapper


@uppercase_decorator
def say_hello():
    return "hello, world!"


print(say_hello())  # "HELLO, WORLD!"

"""
2. Создайте декоратор repeat(n), который выполняет функцию n раз.
Пример вызова:
@repeat(3)
def hello():
    print("Hello!")
hello()
Вывод:
Hello!
Hello!
Hello!
===============================================
"""


def repeat(n):
    def func(func):
        def wrapper():
            for _ in range(n):
                func()

        return wrapper

    return func


@repeat(3)
def hello():
    print("Hello!")


hello()

"""
3. Создайте декоратор cache, который кэширует результаты выполнения функции.
Если функция вызывается с теми же аргументами – возвращать сохраненный результат вместо нового вычисления.
Пример вызова:
@cache
def slow_add(a, b):
    print(f"Вычисляю {a} + {b}...")
    return a + b
print(slow_add(2, 3))  # "Вычисляю 2 + 3..." 5
print(slow_add(2, 3))  # 5 (результат взят из кэша)
===============================================
"""


def cache(func):
    dct_cache = {}

    def wrapper(*args):
        my_key = tuple(sorted(list(args)))
        if my_key in dct_cache:
            return dct_cache[my_key]
        else:
            dct_cache[my_key] = func(*args)
            return dct_cache[my_key]
    return wrapper


@cache
def slow_add(a, b):
    print(f"Вычисляю {a} + {b}...")
    return a + b


print(slow_add(2, 3))  # "Вычисляю 2 + 3..." 5
print(slow_add(2, 3))  # 5 (результат взят из кэша)

"""
4. Создайте декоратор с таймером timer(repeat), который выполняет функцию repeat раз и выводит среднее время выполнения.
Пример вызова:
@timer(3)
def slow_function():
    time.sleep(1)
slow_function()  # Среднее время выполнения: 1.0002 сек
"""


def timer(repeat):
    def inner(func):
        def wrapper():
            lst_res = []
            for _ in range(repeat):
                st_time = time.time()
                func()
                res_time = time.time() - st_time
                lst_res.append(res_time)
            ans = sum(lst_res) / len(lst_res)
            print(f"mean time is {ans}")
        return wrapper
    return inner


@timer(3)
def slow_function():
    time.sleep(1)


slow_function()  # Среднее время выполнения: 1.0002 сек

