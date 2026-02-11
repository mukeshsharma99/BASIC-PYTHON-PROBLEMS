# count vowels and consonants in a string

String = str(input("Enter the string :"))
vowels = "aeiouAEIOU"
v = c = 0
for ch in String:
    if ch.isalpha():
        v += 1
    else:
        c += 1
print("Vowles", v)
print("Consonants", c) 