"""ASS7 PROG1
Program 1:Create a program that ask for a sentence as input.
Display the number of words, vowels and consonants in the input 
ex.
input: Bahala kayo dyan
output:
words: 3
vowels: 6
consonants: 8"""

#Ass7 Prog1, 1st try,   finished the outline, not yet fully working
#                       mali bilang pag may uppercase at may special chars
#            2nd try,   added .lower() for uppercase and a conditional for special chars 
#                       mali bilang pag may number, or extra spaces sa start or end or double splace 
#            3rd try,   added number of characters and special characters in display, added .strip() n .replace() n .join(.split()) and a conditional for numbers, added comments


def AskInput():
    InputSentenceL = str(input("\nHey, enter a SENTENCE and I'll do a word count! \nYour sentence:   "))
    return InputSentenceL

def Counter(InputSentenceL):
    NumVowelL = 0
    NumWordL = 1                # start sa 1 ang count sa word kasi nakabase sya sa space
    NumConsonantL = 0
    NumSpecL = 0

    InputSentenceL = InputSentenceL.lower()                             # nilowercase para d na tatype ung uppercase sa conditionals
    InputSentenceStrippedL = InputSentenceL.strip()                     # inisitrip para d macount ung extra spaces sa simula at sa dulo
    InputSentenceStrippedL = " ".join(InputSentenceStrippedL.split())   # incase lng na may may type ng double space para d macount as 2 words
    InputSentenceNoSpaceL = InputSentenceL.replace(" ", "")             # remove lahat ng space kasi gagamitin tong variable sa pagbilang ng characters without space

    for character in InputSentenceStrippedL:
        if character == " ":                                            #space ung binilang para sa word tas start sa 1 nlng
            NumWordL = NumWordL + 1
        elif character == "a" or character == "e" or character == "i" or character == "o" or character == "u":
            NumVowelL = NumVowelL + 1

        #ung mga sikat na special chars lng nalagay ko, macocount sa consonant kapag gumamit ng spec char na d nasama rito
        elif character == "." or character == "?" or character == "," or character == "!" or character == "'" or character == '"' or character == "&" or character == ";" or character == ":" or character == "-" or character == "_" or character == "’" or character == ")" or character == "(":        
            NumSpecL = NumSpecL + 1

        #incase lng na may mag-enter ng numbers
        elif character == "0" or character == "1" or character == "2" or character == "3" or character == "4" or character == "5" or character == "6" or character == "7" or character == "8" or character == "9":
            pass

        #ginawa kong else ung consonant kasi nakakatamad itype lahat
        else:                                                         
            NumConsonantL = NumConsonantL + 1

    
    NumCharWithSpaceL = len(InputSentenceL)
    NumCharL = len(InputSentenceNoSpaceL)                               # ung no spaces na variable ang cinount 

    return NumVowelL, NumWordL, NumConsonantL, NumCharL, NumCharWithSpaceL, NumSpecL

def Display(NumVowelL, NumWordL, NumConsonantL, InputSentenceL, NumCharL, NumCharWithSpace, NumSpecL ):
    print("\nResults:")
    print(f"Your sentence input:            {InputSentenceL}")
    print()
    print(f"Number of words:                {NumWordL}")
    print(f"Number of vowels:               {NumVowelL}")
    print(f"Number of consonants:           {NumConsonantL}")
    print(f"Number of special characters:   {NumSpecL}")
    print()
    print(f"Number of characters(no spaces):          {NumCharL}")
    print(f"Number of characters(including spaces):   {NumCharWithSpace}")
    print()


if __name__ == "__main__":

    #1 Ask for sentence input
    InputSentence = AskInput()

    #2 Count number of words, vowels, consonants and others
    NumVowel, NumWord, NumConsonant, NumChar, NumCharWithSpace, NumSpec = Counter(InputSentence)

    #3 Display number of words, vowels, consonants and others
    Display(NumVowel, NumWord, NumConsonant, InputSentence, NumChar, NumCharWithSpace, NumSpec)