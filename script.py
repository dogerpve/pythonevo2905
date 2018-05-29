# 1)Дано число. Если оно больше 10, то вывести его на консоль, если же оно меньше 5,
# то увеличить его на 11 и проверить стало ли оно больше 13 если стало вывести
# на консоль «стало больше 13» в противном случае вывести число после сложения,
# в остальных случаях уменьшить число на 100 и проверить что это число находится
# в промежутке между -200 и -50 то выводим этот промежуток и число иначе
# выводим просто число с текстом «Что то пошло на право».

num = int(input("Enter number: "))

if num > 10:
    print('Number more than 10 \nthis number is {}'.format(num))
elif 0 < num < 5:
    if num + 11 > 13:
        print('Number more than 13 \nThis number now {}'.format(num + 11))
    else:
        print('Number less than 5 \nThis number now {}'.format(num + 11))
else:
    if (num - 100) > -200 and num - 100 < -50:
        print('Number between -200 and -50 \nThis number now {}'.format(
            num - 100
            )
        )
    else:
        print('Что то пошло на право {}'.format(num))

# 2)Выведите на экран n раз фразу "Silence is golden". Число n вводит пользователь.

n_number = int(input('Enter count number: '))

print(' Silence is golden ' * n_number)