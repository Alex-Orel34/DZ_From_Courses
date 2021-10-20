# First solution with using of 'for'

ls = list(map(int, input().split()))
ls_result = []
for i in range(len(ls)):
    ls_result.append(ls[i] * -2)
print(ls_result)

# Second solution with using of 'while'

ls1 = list(map(int, input().split()))
ls_result1 = []
i=0
while i<len(ls1):
    ls_result1.append(ls1[i] * -2)
    i+=1
print(ls_result1)

