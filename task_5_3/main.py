def Friend(x):
    k = 0
    for i in range(1, x - 1):
        if x % i == 0:
            k += i
    return k


for i in range(200, 300):
    for j in range(200, 300):
        if Friend(i) == j and i == Friend(j):
            print(f'{i} -- {j}')
