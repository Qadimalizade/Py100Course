def is_palindrome(text):
    text = ''.join(text.lower().split())
    return text == text[::-1]

print(is_palindrome("радар"))
print(is_palindrome("А роза упала на лапу Азора"))
