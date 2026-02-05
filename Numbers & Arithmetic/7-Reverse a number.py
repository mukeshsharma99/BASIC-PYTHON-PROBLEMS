# Reverse a number.

num = int(input("Enter the number: "))
reverse = 0

while num >0 :
    reverse  = reverse * 10 + num %10
    num //= 10

print("Reversed Number", reverse)