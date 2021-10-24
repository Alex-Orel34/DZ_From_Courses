import random

n,m = list(map(int,input('Put sizes of matrix: ').split()))
Matrix = [[random.randint(1, 9) for j in range(n)]for i in range(m)]
for i in range(m):
    for j in range(n):
        print(Matrix[i][j],end=' ')
    print()
print()
ls=[]
indexes=[]
for row in Matrix:
    ls.append(max(row))
    indexes.append(row.index(max(row)))
for i in range(n):
    r=Matrix[i][i]
    Matrix[i][i]=ls[i]
    Matrix[i][indexes[i]]=r

for i in range(m):
    for j in range(n):
        print(Matrix[i][j],end=' ')
    print()
