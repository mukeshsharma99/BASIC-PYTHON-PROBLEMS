# number is a palindrome

num=  int(input("Enter the number: "))
temp  = num
reverse = 0

while num > 0:
    reverse = reverse *10 + num %10
    num //= 10

if temp == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")

