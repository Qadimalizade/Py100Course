sum_ = 0  # заводим переменную счетчик, в которой мы будем считать сумму
n = 1  # текущее натуральное число
max_sum = 250

# заводим цикл while, который будет работать пока сумма не превысит 250
while True:
    if sum_ > max_sum:  # если сумма превысила нужное значение, то останавливаем цикл
        break
    sum_ += n
    n += 1  # так как сумма ещё не достигла нужного значения, то увеличиваем переменную счетчик
    print("Ещё считаю ...", sum_)

print("Количество чисел: ", n)