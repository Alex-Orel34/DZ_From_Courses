def fact2(n):
    answ = 1
    for i in range((1 if n % 2 else 2), n + 1, 2):
        answ *= i
    return answ


n = int(input())
print(fact2(n))