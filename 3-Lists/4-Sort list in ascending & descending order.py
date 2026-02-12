# Sort list in ascending & descending order

num = list(map(int, input("Enter the number : ").split()))

num.sort()
print("Ascending", num)

num.sort(reverse=True)
print("Descending", num)