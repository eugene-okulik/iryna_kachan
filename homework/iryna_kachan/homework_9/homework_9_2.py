temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22,
                22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]
hot = list(filter(lambda x: x > 28, temperatures))
avg_temp = sum(hot) / len(hot)
print(max(hot))  # highest temp
print(min(hot))  # lowest temp
print(avg_temp)  # average temp
