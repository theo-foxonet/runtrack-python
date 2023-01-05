import random
L = []
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(5):
    L.append(random.choice(list))
print(L)

print(L[1])

def replace(list):
    if len(list) >= 5:
        list[3] = list[2] + list[4]
    return list
print(replace(L))

print(L[-1])