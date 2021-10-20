# First solution with using of 'for'

ls = list(map(int, input().split()))
n = 0
for i in range(len(ls)):
    if ls[i] % 2 == 0:
        n += 1
print(n)

# Second solution with using of 'while'

ls1 = list(map(int, input().split()))
n1 = 0
i=0
while i< len(ls1):
    if ls[i] % 2 == 0:
        n1 += 1
    i+=1
print(n1)