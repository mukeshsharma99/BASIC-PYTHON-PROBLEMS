string1 = input("Enter the string1: ")
string2 = input("Enter the string2: ")

if sorted(string1) == sorted(string2):
    print("Anagrams")
else:
    print("Not Anagrams")