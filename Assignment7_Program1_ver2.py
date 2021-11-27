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
#                       mali bilang sa consonants, at mali bilang pag may uppercase at may special chars 
#            2nd try,   working, fixed consonants, added .lower() for uppercase and a conditional for special chars 

def AskInput():
    InputSentenceL = str(input("\nHey, enter a SENTENCE and I'll tell you how many words, vowels, and constants there are! \nYour sentence:   "))
    return InputSentenceL

def Counter(InputSentenceF):
    NumVowelL = 0
    NumWordL = 0
    NumConsonantL = 0

    InputSentenceF = InputSentenceF.lower()
    
    for character in InputSentenceF:
        if character == " ":
            NumWordL = NumWordL + 1
        if character == "a" or character == "e" or character == "i" or character == "o" or character == "u":
            NumVowelL = NumVowelL + 1
        elif character != " " and character != "." and character != "?" and character != "," and character != "!" and character != "'" and character != '"' and character != "&":
            NumConsonantL = NumConsonantL + 1
    NumWordL = NumWordL + 1

    return NumVowelL, NumWordL, NumConsonantL

def Display(NumVowelL, NumWordL, NumConsonantL, InputSentenceL):
    print(f"\nYour sentence input:   {InputSentenceL}")
    print(f"Number of words:   {NumWordL}")
    print(f"Number of vowels:   {NumVowelL}")
    print(f"Number of consonants:   {NumConsonantL}")
    print()

#1 Ask for sentence input
InputSentence = AskInput()
#2 Count number of words, vowels, and consonants
NumVowel, NumWord, NumConsonant = Counter(InputSentence)

#3 Display number of words, vowels, and consonants
Display(NumVowel, NumWord, NumConsonant, InputSentence)
