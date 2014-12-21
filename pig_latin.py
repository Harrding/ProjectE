#This program is to receive an input and change the words into pig latin
"""
    Rules for pig latin:
    Words that begin with a consonant is moved to
        the end of the word, and "ay" is added
    Words that begin with a vowel or silent letter,
        you just add "way" to the end
"""

originalString = input("Enter the word you desire to be translated into pig latin :\n")
originalString = originalString.lower()
lStrippedString = originalString.lstrip('aeiou')
latinString = ""
if len(originalString) > len(lStrippedString) :
    latinString = originalString + "way"
else:
    latinString = originalString[1:]+originalString[0]+"ay"
print("\nYour pig latin string is : " + latinString.capitalize() + "\n\n")
