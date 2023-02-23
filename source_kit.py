"""
Реализуйте функцию print_kit() и вызовите в ней все функции,
которые определены в модуле kit.py. Предварительно импортируйте их.
"""

from kit import show_language, say_hello, say_bye


def print_kit():
    show_language()
    say_hello()
    say_bye()


print_kit()