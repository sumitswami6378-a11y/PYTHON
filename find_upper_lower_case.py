string = input("ENTER THE STRING = ")

upper = 0
lower = 0

for ch in string :
    if ch >= "A" and ch <= "Z" :

        upper = upper + 1

    elif ch >= "a" and ch <= "z" :

        lower = lower + 1

print("THE UPPER CASE LETTER IS = ", upper)
print("THE LOWER CASE LETTER IS = ", lower)


