"""
Реализуйте функцию choice_from_range(), которая принимает строку-набор и
возвращает случайный символ по индексу из ограниченного диапазона.

Аргументы функции:

строка-набор
начальный индекс диапазона
конечный индекс диапазона
"""
import random


def choice_from_range(text, start, finish):
    index = random.randint(start, finish)
    return text[index]


text = "abcdef"
print(choice_from_range(text, 3, 5))  # d
print(choice_from_range(text, 3, 5))  # f
print(choice_from_range(text, 3, 5))  # e
