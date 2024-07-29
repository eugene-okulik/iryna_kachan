import random
salary = int(input())
bonus = random.choice([False, True])
if bonus is True:
    total_salary = salary + random.randint(1, 50000)
    print(f"{salary}, {bonus} - '${total_salary}'")
else:
    print(f"{salary}, {bonus} - '${salary}'")
