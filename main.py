# Преобразуем строку в нижний регистр и удаляем лишние символы
# Сравниваем полученную строку с ее обратной версией

def is_palindrome(string):
    cleaned_string = ''.join(filter(str.isalnum, string.lower()))
    return cleaned_string == cleaned_string[::-1]

print(is_palindrome("A man, a plan, a canal, Panama"))  # True
print(is_palindrome("hello"))  # False
