def fib(n):
    a, b = 0, 1
    for num in range(n):
        yield a
        a, b = b, a + b


def print_fib(num):
    count = 1
    if num == 0:
        print(0)
    else:
        for number in fib(1000000):
            if count == num:
                print(number)
                break
            count += 1


print_fib(5)
print_fib(200)
print_fib(1000)
print_fib(100000)  # ValueError: Exceeds the limit (4300 digits) for integer string conversion
