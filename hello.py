n = 1
for i in range(1, 5):
    for j in range(1, 6):
        if i % 2 == 1:
            print(n, end=" ")
        elif i % 2 == 0:
            print((i * 5) - j + 1, end=" ")
        n += 1
    print()