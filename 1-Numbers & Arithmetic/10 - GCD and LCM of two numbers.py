# GCD and LCM of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# GCD
x, y = a, b
while y != 0:
    x, y = y, x % y
gcd = x

# LCM
lcm = (a * b) // gcd

print("GCD =", gcd)
print("LCM =", lcm)
