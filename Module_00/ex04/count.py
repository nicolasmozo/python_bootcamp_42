import sys
import string

def text_analyzer(word=None):
    '''
    This function counts the number of upper characters, lower characters, punctuation and spaces in a given text. 
    '''
    if word == None:
        word = input("What is the text to analyze? ")

    if type(word) != str:
        print("AssertionError: argument is not a string")
        return

    print("The text contains ", sum(1 for char in word), "character(s):")
    print("- ", sum(1 for char in word if char.isupper()), " upper letter(s)")
    print("- ", sum(1 for char in word if char.islower()), " lower letter(s)")

    marks = 0
    for i in word:
        for j in string.punctuation:
            if i == j:
                marks += 1
    print("- ", marks, " punctuation mark(s)")

    spaces = 0
    for i in word:
        if i == " ":
            spaces += 1
    print("- ", spaces, " space(s)")

x = sys.argv
if len(x) > 2:
    print("AssertionError: More than one argument")
elif len(x) == 2:
    text_analyzer(x[1])