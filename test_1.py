import re

"""
А вот наиболее популярные методы, которые предоставляет модуль:

re.match()
re.search()
re.findall()
re.split()
re.sub()
re.compile()
"""

# re.match(pattern, string)
# Этот метод ищет по заданному шаблону в начале строки.
print(f're.match(pattern, string) Этот метод ищет по заданному шаблону в начале строки.')
print('*' * 80)
result = re.match(r'AV', 'AV Analytics Vidhya AV')
print(result)
print('*' * 80)
print(result.group(0))
print('*' * 80)
result = re.match(r'Analytics', 'AV Analytics Vidhya AV')
print(result)
print('*' * 80)
result = re.match(r'AV', 'AV Analytics Vidhya AV')
print(result.start())
print(result.end())
print('*' * 80)
print(f're.search(pattern, string) Метод похож на match(), но ищет не только в начале строки.')
result = re.search(r'Analytics', 'AV Analytics Vidhya AV')
print(result.group(0))
# Метод search() ищет по всей строке, но возвращает только первое найденное совпадение.
print('*' * 80)
print('re.findall(pattern, string) Возвращает список всех найденных совпадений. '
      'У метода findall() нет ограничений на поиск в начале или конце строки.')
result = re.findall(r'AV', 'AV Analytics Vidhya AV')
print(result)
print('*' * 80)
print('re.split(pattern, string, [maxsplit=0]) Этот метод разделяет строку по заданному шаблону.')
result = re.split(r'y', 'Analytics')
print(result)
print('*' * 80)
result = re.split(r'i', 'Analytics Vidhya')
print(result)
print('*' * 80)
result = re.split(r'i', 'Analytics Vidhya', maxsplit=1)
print(result)
print('*' * 80)
print('re.sub(pattern, repl, string) Ищет шаблон в строке и заменяет его на указанную подстроку. Если шаблон не '
      'найден, строка остается неизменной.')
print('*' * 80)
result = re.sub(r'India', 'the World', 'AV is largest Analytics community of India')
print(result)
print('*' * 80)
print('re.compile(pattern, repl, string) Мы можем собрать регулярное выражение в отдельный объект, который может быть '
      'использован для поиска. ')
pattern = re.compile('AV')
result = pattern.findall('AV Analytics Vidhya AV')
print(result)
result2 = pattern.findall('AV is largest analytics community of India')
print(result2)
print('*' * 80)

