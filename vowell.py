string = input("ENTER THE STRING = ")
count = 0
for char in string:
    if char in"AEIOUaeiou ":
        count = count + 1

print(count)