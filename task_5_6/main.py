import random

n = int(input())
ls = [random.randint(1, 11) for i in range(n)]
print(ls)
k = 0
for i in range(2,n):
    if ls[i] > ls[i - 1]>ls[i-2]:
        k+=1
    elif ls[i - 1]>ls[i-2]:
        k+=1
print(k)
