sentence = input()


upper = 0
lower = 0


for i in sentence:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1


print("UPPER CASE", upper, "LOWER CASE", lower)
