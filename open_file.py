"""
    This python file is used to be imported so that the user will
    have the function of either asking the user for an input or
    using an input that is implemented in its args as the file it
    will be opening.
    args []
    [0] = file name
    [1] = append, read, 
"""
import os
def openFile (*args) :
    if len(args) >= 2:
        if len(args) == 3 :
            os.chdir(args[2])
        fo = open(args[0], args[1])
        return fo
    else :
        return None
"""fo = openFile("test.txt", "r", "txt_files")
string = fo.read()
print(string)
"""
