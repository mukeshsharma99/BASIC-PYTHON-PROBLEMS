# Split the number into the even and odd using the list 

nums = list(map(int, input("Enter the numbers: ").split()))

even = [x for x in nums if x % 2 == 0]
odd = [x for x in nums if x % 2 != 0]

print("Odd:", odd)
print("Even:", even)
