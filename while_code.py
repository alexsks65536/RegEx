def greet():
    count = 0
    while True:
        print('Hello!')
        count += 1


# greet()


def print_numbers(n):
    while n >= 1:
        print(n)
        n -= 1

    print("finished!")


# print_numbers(4)

def sum_numbers_from_range(start, finish):
    # Технически можно менять start
    # Но входные аргументы нужно оставлять в исходном значении
    # Это сделает код проще для анализа
    i = start
    sum = 0  # Инициализация суммы
    while i <= finish:  # Двигаемся до конца диапазона
        sum = sum + i   # Считаем сумму для каждого числа
        i = i + 1       # Переходим к следующему числу в диапазоне
    # Возвращаем получившийся результат
    print(f'Сумма чисел равна: {sum}')


# sum_numbers_from_range(1, 10000)


def repeat(text, times):
    # Нейтральный элемент для строк — пустая строка
    result = ''
    i = 1

    while i <= times:
        # Каждый раз добавляем строку к результату
        result = result + text
        i = i + 1

    print(f'Результат: {result}')


# repeat('someone', 3)


def multiply_numbers_from_range(start, finish):
    i = start
    multiply = 1

    while i <= finish:
        multiply *= i
        i += 1
    print(f'Результат умножения: {multiply}')


# multiply_numbers_from_range(3, 5)  # 60


def join_numbers_from_range(start, finish):
    i = start
    summ = ''
    while i <= finish:
        summ += str(i)
        i += 1
    return summ
    # print(f'Результат: {summ}')


# print(join_numbers_from_range(5, 10))


def print_name_by_symbol(name):
    i = 0
    # Такая проверка будет выполняться до конца строки,
    # включая последний символ. Его индекс `length - 1`.
    while i < len(name):
        # Обращаемся к символу по индексу
        print(name[i])
        i += 1


# name = 'Arya'
# print_name_by_symbol(name)


def reverse_string(string):
    index = len(string) - 1
    reversed_string = ''

    while index >= 0:
        current_char = string[index]
        reversed_string = reversed_string + current_char
        # То же самое через интерполяцию
        # reversed_string = f'{reversed_string}{current_char}'
        index = index - 1

    return reversed_string


# print(reverse_string('Game Of Thrones'))  # 'senorhT fO emaG'
# Проверка нейтрального элемента
# reverse_string('')  # ''


def my_substr(string, n):
    length_of_str = n - 1
    result = ''
    i = 0
    while i <= length_of_str:
        result += string[i]
        i += 1

    return result


# string = 'Ехал Грека через реку'
# print(f'Результат: {my_substr(string, 8)}')


def count_chars(string, char):
    index = 0
    count = 0
    while index < len(string):
        if string[index] == char:
            # Считаем только подходящие символы
            count = count + 1
        # Счетчик увеличивается в любом случае
        index = index + 1
    return count


# char = 'е'
# print(f'Кол-во символов "{char}" в строке - "{string}": {count_chars(string, char)}')

"""
Рассмотрим алгоритм проверки простоты числа. 
Будем делить искомое число x на все числа из диапазона от двух до x - 1 
и смотреть остаток. Если в этом диапазоне не найден делитель, 
который делит число x без остатка, значит, перед нами простое число.
"""


def is_prime(number):
    if number < 2:
        return False

    divider = 2

    while divider <= number / 2:
        if number % divider == 0:
            return False

        divider += 1

    return True


# print(is_prime(1))  # => False
# print(is_prime(2))  # => True
# print(is_prime(3))  # => True
# print(is_prime(4))  # => False


def is_contains_char(string_1, letter):
    str = string_1.lower()
    i = 0
    length = len(str) - 1
    while i <= length:
        if str[i] == letter.lower():
            return True
        i += 1

    return False


# print(is_contains_char('Hexlet', 'H'))  # => True
# print(is_contains_char('Hexlet', 'e'))  # => True
# print(is_contains_char('Awesomeness', 'd'))  # => False
# print(is_contains_char('Awesomeness', 'm'))

def to_upper(text):
    for char in text[::-1]:
        print(char.upper())


# to_upper('hello')


def filter_string(text, letter):
    low_char = letter.lower()
    result_string = ''
    for i in text:
        if i.lower() != low_char:
            result_string += i
    print(result_string)


# text = '   If I look forward I win   '
# filter_string(text, 'i')  # 'f  look forward  wn'
# filter_string(text, 'O')  # 'If I lk frward I win
# filter_string(text, 'W')
#
# text = 'I look back if you are lost'
# filter_string(text, 'w')
# filter_string(text, 'W')


def is_palindrome(text):

    f_text = text.replace(' ', '').lower()  # соединяем в одну строку без пробелов
    f_length = len(f_text)  # длина строки
    half_length = f_length // 2  # находим длину половины текста

    if f_length % 2 == 0:  # если кол-во символов в строке четное
        left_text = f_text[0:half_length]  # левая половина строки
        right_text = f_text[half_length:len(f_text)]  # правая половина строки
        right_text = right_text[::-1]  # переворот строки
        if left_text == right_text:  # если левая половина равна перевернутой правой
            return True
        return False
    else:  # если кол-во символов нечетное
        half_length += 1
        left_text = f_text[0:half_length]  # левая половина строки
        right_text = f_text[half_length - 1:len(f_text)]  # правая половина строки
        right_text = right_text[::-1]  # переворот строки
        if left_text == right_text:  # если левая половина равна перевернутой правой
            return True
        return False


def is_palindrome_1(string):
    string = string.replace(' ', '').lower()
    pointer1 = 0
    pointer2 = len(string) - 1
    while pointer2 - pointer1 > 0:
        if string[pointer1] != string[pointer2]:
            return False
        pointer1 += 1
        pointer2 -= 1
    return True


def is_palindrome_2(string):
    string = string.replace(' ', '').lower()
    return string == string[::-1]


test_string = ['', 'radar', 'a', 'abs', 'ишак ищет у тещи каши', 'abba', 'А роза упала на лапу Азора']
for i in test_string:
    print(f'"{i}" 1: {is_palindrome(i)}, 2: {is_palindrome_1(i)}, 3: {is_palindrome_2(i)}')
