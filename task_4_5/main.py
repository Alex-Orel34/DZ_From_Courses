# First solution with using of 'for'

ls=[1,1]
for i in range(1,14):
    ls.append(ls[i-1]+ls[i])
print(ls)

# Second solution with using of 'while'

ls1=[0,1]
i=1
while i<14:
    ls1.append(ls1[i-1]+ls1[i])
    i+=1
print(ls1)