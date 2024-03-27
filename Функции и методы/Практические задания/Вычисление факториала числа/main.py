def factorial(n):
    total = 1
    for i in range(1, n+1):
        total *= i
    return total


# TODO Вызовите функцию factorial и распечатайте результат 
print(f"Факториал числа 0 равен {factorial(0)}")
print(f"Факториал числа 5 равен {factorial(5)}")
