# First solution with using of 'for'

dictt = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
for key in list(dictt.keys()):
    dictt[key + str(len(key))] = dictt.pop(key)
print(dictt)

# Second solution with using of 'while'

dictt_1 = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
ls = list(dictt_1.keys())
i = 0
while i < len(ls):
    dictt_1[ls[i] + str(len(ls[i]))] = dictt_1.pop(ls[i])
    i += 1
print(dictt_1)
