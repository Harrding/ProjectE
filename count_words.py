"""
    The user will be able to input a string for this program
    to count the number of words they have typed.

    Challenge: If they enter a string with .txt, the program
    will look for a file by the name of ___.txt and read every
    word of it and count the number of words that exist in the
    text file.
"""

import ask_question, open_file

stringInput = ask_question.getString("Enter the string or the text file name that" +
                                     " you desire to have the number of words be counted")

def countWords(sentence):
    wordCount = 0
    currentWord = False
    for x in sentence:
        if currentWord and (x == " " or x == "\n") :
            currentWord = False
        elif (not currentWord) and (x == " " or x == "\n"):
            currentWord = False
        else:
            if not currentWord:
                wordCount+=1
            currentWord = True
    return wordCount
currentCount = countWords(stringInput)
if currentCount == 1 and stringInput.find(".txt"):
    fo = open_file.openFile(stringInput,"r", "txt_files")
    stringInput = fo.read()
    
print("\n\nThe number of words that exists is : " + str(countWords(stringInput)))
        
        

