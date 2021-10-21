# First solution with using of 'for'

ls = list(map(int, input().split()))
a=ls[0]
ls_result = []
for i in range(1, len(ls)):
    ls_result.append(ls[i])
ls_result.append(a)
print(ls_result)

# Second solution with using of 'while'

ls1 = list(map(int, input().split()))
ls_result1 = []
i=1
a=ls1[0]
while i < len(ls1):
    ls_result1.append(ls1[i])
    i+=1
ls_result1.append(a)
print(ls_result1)
