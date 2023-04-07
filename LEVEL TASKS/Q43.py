tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

list = []


for i in tuple:
    if i % 2 == 0:
        list.append(i)


eventuple = tuple(list)


print(eventuple)
