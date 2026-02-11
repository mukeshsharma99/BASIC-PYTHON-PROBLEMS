import string

s = input("Enter the string: ")

result = ""

for ch in s:
    if ch not in string.punctuation:
        result += ch

print(result)
