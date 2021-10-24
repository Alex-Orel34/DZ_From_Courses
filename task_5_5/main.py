import random

ls=[random.randint(1,100) for i in range(19)]
max_digit= max(ls)
print(f'Max digit in array is {max_digit}')
for i in range(19):
    if i%2==0:
        ls[i]=max_digit
print(ls)
