""" This program is used to receive an input from the user and
    print out true or false on whether or not the input is a
    palindrome or not."""

palindromeString = input("\n\nEnter a string to check if it is a palindrome : ")
def checkPalindrome(palindromeValue):
    checkString = ""
    palindromeValue = palindromeValue.lower()
    for char in palindromeValue:
        checkString = char + checkString
    if palindromeValue == checkString:
        return True
    return False

if checkPalindrome(palindromeString):
    print ("\n\nValue you entered is a palindrome.\n\n")
else:
    print ("\n\nThe value you entered is not a palindrome.\n\n")
    
