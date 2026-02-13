# 7-sum of all elements in a list.py

num  = list(map(int, input("Enter the Number: ").split()))

total = 0

for number in num:
    total += number

print("Sum", total)