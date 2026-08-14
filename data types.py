x = [1, 1, 1, 3, 2, 1, 1, 1, 1, 10]

largest = x[0]

for i in range(len(x)):
    if x[i] > largest:
        largest = x[i]
