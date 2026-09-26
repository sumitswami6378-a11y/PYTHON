text = " python or java "

character = 0
for ch in text:
    character = character + 1
print(character)

vowel = 0
for v in text:
    if v in "AEIOUaeiou" :

     vowel = vowel + 1
print(vowel)

con = 0
for consonant  in text :
   if consonant not in "AEIOUaeiou" :

      con = con + 1
print(con)


for vow in text :
   if vow in "AEIOUaeiou":
      print(vow)


for consonant in text:
   if consonant not in "AEIOUaeiou":
      print(consonant)

find = input("enter the finding character= ")
cou = 0
for ch in text:
   if ch == find:
      cou = cou + 1

print("count of particular =", cou)