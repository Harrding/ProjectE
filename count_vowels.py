""" The user enters a string to check the number of vowels that exist
    within the string. Then this program will display the number of
    a :
    e :
    i :
    o :
    u :
    vowels.
"""

    
import ask_question

check = ask_question.getString("Enter the string you desire to have checked for number of vowels")
check = check.lower()
def countNumLetter(charValue, stringValue):
    count = 0
    for x in stringValue:
        if x == charValue:
            count+=1
    return count

def displayCount(char, stringValue):
    charValue = char
    print("\nThe number of %s is : " %(charValue), end="")
    print(countNumLetter(charValue, stringValue))

displayCount('a', check)
displayCount('e', check)
displayCount('i', check)
displayCount('o', check)
displayCount('u', check)
print("\n\n")


"""
Notes:
    You can import a file from the current directory. I'm not too
    sure as to how to import from parent directories but I have a
    suspicion you can do that with import parent.? Not too sure
    though. Also, there cannot be multiple methods with the same
    name. The only method of doing this is by passing in an array
    of args in which case the method will have to do things on its
    own to separate the values.
"""
