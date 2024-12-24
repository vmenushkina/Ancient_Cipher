def get_cipher(n):
    result = ''
    for i in range(1, n):
        for j in range(i+1, n):
            if n % (i + j) == 0:
                result += str(i) + str(j)

    return f'Число на камне в первом поле {n} - пароль {result}\n'

print('Введите целое число от 3 до 20: ')
print(get_cipher(int(input())))