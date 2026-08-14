for i in range(3):
    print("Hello")
for i in range(5):
    print("Number:", i)
for i in range(5):
    print(i)
for i in range(3, 9):
    print(i)
for i in range(0, 11, 2):
    print(i)
for i in range(1, 6):
    print(i * 10)
for i in range(1, 11):
    print("2 x", i, "=", 2 * i)
for i in range(1, 5):
    print(i * 2)
for i in range(3):
    for j in range(3):
        print(i, j)
for i in range(10):
    if i == 5:
        break
    print(i)
for i in range(5):
    if i == 2:
        continue
    print(i)
i = 1

while i <= 5:
    print(i)
    i = i + 1