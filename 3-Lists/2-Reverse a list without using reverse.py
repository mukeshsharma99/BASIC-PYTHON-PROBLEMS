# Reverse a list without using reverse() method.

nums = list(map(int, input("Enter the numbers: ").split()))

rev = []
for i in range(len(nums) - 1, -1, -1):
    rev.append(nums[i])

print("Reversed list:", rev)
