digit = int(input())
s = 1
for i in range(2, digit):
    s += 1 / i
print(s)
