line_1 = 'результат операции: 42'
line_2 = 'результат операции: 54'
line_3 = 'результат работы программы: 209'
line_4 = 'результат: 2'
def calc(line):
    number = int(line[line.index(':') + 2:]) + 10
    return(print(number))
calc(line_1)
calc(line_2)
calc(line_3)
calc(line_4)
