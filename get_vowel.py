from symbols import is_vowel


def count_vowels(text):
    result = 0
    for char in text:
        if is_vowel(char):
            result += 1
    return result


print(count_vowels('При использовании паттерна'))