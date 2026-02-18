# Rotate list right by k

nums = list(map(int, input("Enter the number for the lsit: ").split()))

k = 2

k %= len(nums)
print(nums[-k:] + nums[:-k])