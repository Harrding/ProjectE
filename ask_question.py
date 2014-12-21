"""
    This file will be used to define the method of asking questions and
    receiving a string as the input.
"""

def getString(*args):
    if len(args) > 0:
        return input("\n\n" + args[0] + " : " )
    else :
        return input("\n\nPlease enter a string : ")
