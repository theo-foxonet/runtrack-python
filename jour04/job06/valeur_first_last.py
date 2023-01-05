import random
L = []
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(5):
    L.append(random.choice(list))
print(L)

def exchange(list):
    if len(list) >= 2:
        index = list[0]
        list[0] = list[-1]
        list[-1] = index
    return list
print(exchange(L))