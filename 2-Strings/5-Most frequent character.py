# Find the most frequent character in a string.

string = input("Enter the string: ")
max_char = ""
max_count =0

for ch in string:
    count = string.count(ch)
    if count > max_count:
        max_char  = ch

print(max_char, max_count)

