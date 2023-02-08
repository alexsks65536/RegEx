"""
    Оператор	Описание
    .	Один любой символ, кроме новой строки \n.
    ?	0 или 1 вхождение шаблона слева
    +	1 и более вхождений шаблона слева
    *	0 и более вхождений шаблона слева
    \w	Любая цифра или буква (\W — все, кроме буквы или цифры)
    \d	Любая цифра [0-9] (\D — все, кроме цифры)
    \s	Любой пробельный символ (\S — любой непробельный символ)
    \b	Граница слова
    [..]	Один из символов в скобках ([^..] — любой символ, кроме тех, что в скобках)
    \	Экранирование специальных символов (\. означает точку или \+ — знак «плюс»)
    ^ и $	Начало и конец строки соответственно
    {n,m}	От n до m вхождений ({,m} — от 0 до m)
    a|b	Соответствует a или b
    ()	Группирует выражение и возвращает найденный текст
    \t, \n, \r	Символ табуляции, новой строки и возврата каретки соответственно
"""
import re


class Separator:

    def __init__(self, result):
        self.result = result

    def output(self):
        print()
        print('*' * 80)

result = re.findall(r'.', 'AV is largest Analytics community of India')

print(result)
print('*' * 80)
# Для того, чтобы в конечный результат не попал пробел, используем вместо . \w.
result = re.findall(r'\w', 'AV is largest Analytics community of India')
print(result)
print('*' * 80)
# Теперь попробуем достать каждое слово (используя * или +)
result = re.findall(r'\w*', 'AV is largest Analytics community of India')
print(result)
#  И снова в результат попали пробелы, так как * означает «ноль или более символов». Для того, чтобы их убрать, используем +:
print('*' * 80)
result = re.findall(r'\w+', 'AV is largest Analytics community of India')
print(result)
print('*' * 80)
# Теперь вытащим первое слово, используя ^:
#
result = re.findall(r'^\w*', 'AV is largest Analytics community of India')
print(result)
print('*' * 80)
# Если мы используем $ вместо ^, то мы получим последнее слово, а не первое:
result = re.findall(r'\w+$', 'AV is largest Analytics community of India')
print( result)
print('*' * 80)

