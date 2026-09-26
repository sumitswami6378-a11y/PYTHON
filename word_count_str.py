word = input("ENTER THE WORD WHICH YOU WANT TO COUNT = ")
string = "this is sumit swami "
count_word = 0
for ch in string:
    if ch == word :
        count_word = count_word + 1

print(count_word)