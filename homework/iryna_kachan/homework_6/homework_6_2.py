user_input = int(input('yor number: '))
for user_input in range(1,101):
    if (user_input % 3 == 0) and  (user_input % 5 == 0):
        print('FuzzBuzz')
    elif user_input % 3 == 0:
        print('Fuzz')
    elif user_input % 5 == 0:
        print('Buzz')
    else:
        print(user_input)
