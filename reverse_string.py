stringInput = input("Enter a string to be reversed:\n")
newString = ""
for x in stringInput:
    newString = x + newString
print(newString)
