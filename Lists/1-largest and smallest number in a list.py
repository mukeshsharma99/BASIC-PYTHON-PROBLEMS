# Find the largest and smallest number in a list

nums = list(map(int, input("Enter numbers separated by space: ").split()))

small = nums[0]
large = nums[0]

for number in nums:
    if number < small:
        small = number
    if number > large:
        large = number

print("Smallest:", small)
print("Largest:", large)
