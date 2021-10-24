digit=int(input())
summary = 0
while digit % 10 != 0:
    summary += digit % 10
    digit = int(digit / 10)

print(summary)