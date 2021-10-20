# First solution with using of 'for'

ls = list(map(int, input().split()))
ls_result = []
for i in range(1, len(ls)):
    ls_result.append(ls[i])
print(ls_result)

# Second solution with using of 'while'

ls1 = list(map(int, input().split()))
ls_result1 = []
i=1
while i < len(ls1):
    ls_result1.append(ls1[i])
    i+=1
print(ls_result1)