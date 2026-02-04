# Write a python  Sum of digits

num  = int(input("Enter the number: "))
sum_digits = 0
while num > 0:
    sum_digits += num % 10
    num //= 10

print("Sum of the digits = ", sum_digits)
