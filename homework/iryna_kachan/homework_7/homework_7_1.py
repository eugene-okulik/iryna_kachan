import random
number = random.randint(0, 9)
while number != int(input()):
    print('попробуйте снова')
else:
    print('Поздравляю! Вы угадали!')
