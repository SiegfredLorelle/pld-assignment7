"""ASS7 PROG2
Program 2: Password validator
Create a program that check if password is valid
The password is valid if all criteria are met:
a. Greater than 15 letters
b. Have at least one capital letter
c. Have at least one number
d. Have at least one special char (!@#$%^&*()_+ etc)
ex.
input: P@ssw0rd+P@ssw0rd
ouput: Valid"""

#Ass7 Prog2, 1st try,   finished checker(), not yet fully working

def AskInput():
    print("\nHey, Register a VALID password to your account.")
    print("VALID password must be:\n  a. Greater than 15 letters,\n  b. Have at least one capital letter,\n  c. Have at least one number,\n  d. And have at least one special character")
    InputPassL = str(input("\nPassword:   "))
    return InputPassL

def Checker( InputPassL):
#Criteria A
    if len(InputPassL) > 15:
        ConditionA = "A Valid"
    else:
        ConditionA = "A Invalid"
    print(ConditionA)

#Criteria B
    UpperCaseCounter = 0
    for character in InputPassL:
        if character.isupper():
            UpperCaseCounter = UpperCaseCounter + 1
    if UpperCaseCounter > 0:
        ConditionB = "B Valid"
    else:
        ConditionB = "B Invalid"
    print(ConditionB)   

#Criteria C
    NumberCounter = 0
    NumberList = [0,1,2,3,4,5,6,7,8,9]
    for character in InputPassL:
        if character in str(NumberList):
            NumberCounter = NumberCounter + 1
    if NumberCounter > 0:
        ConditionC = "C Valid"
    else:
        ConditionC = "C Invalid"
    print(ConditionC)

#Criteria D
    SpecialCharCounter = 0
    SpecialCharList = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "{", "[", "}", "]", "\\", "|", ";", ":", "'",  '"', "<", ",", ">", ".", "/", "?"]
    for character in InputPassL:
        if character in SpecialCharList:
            SpecialCharCounter = SpecialCharCounter + 1
    if SpecialCharCounter > 0:
        ConditionD = "D Valid"
    else:
        ConditionD = "D Invalid"
    print(ConditionD)


if __name__ == "__main__":

    #1 Ask for password input
    InputPass = AskInput()

    #2 Check for validity
    Checker(InputPass)

    #3 Display Valid or inalid

  