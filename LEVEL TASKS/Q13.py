sentence = input()


letters = 0
digits = 0


for i in sentence:
    if i.isalpha():
        letters += 1
    elif i.isdigit():
        digits += 1

print("LETTERS", letters, "DIGITS", digits)
