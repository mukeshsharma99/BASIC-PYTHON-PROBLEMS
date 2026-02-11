# Remove duplicates from a list.

num = list(map(int, input("Enter the numbers: ").split()))

unique = []

for i in num:
    if i not in unique:
        unique.append(i)

print(unique)
