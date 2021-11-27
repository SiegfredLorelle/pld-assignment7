"""ASS7 PROG2
Program 2: Password validator
Create a program that check if password is valid
The password is valid if all criteria are met:
a. Greater than 15 characters
b. Have at least one capital letter
c. Have at least one number
d. Have at least one special char (!@#$%^&*()_+ etc)
ex.
input: P@ssw0rd+P@ssw0rd
ouput: Valid"""

#Ass7 Prog2, 1st try,   finished checker(), not yet fully working
#            2nd try,   finsished display(), added error message, added criteria that there should be no space
#                       removed Invalid Validity (only uses Valid and not equal Valid), put each condition checker to their own def func       
#            3rd try,   loop until maging valid ung password, added comments, changed letters to character in criteria a

def AskInput():
    InputPassL = str(input("\nPassword:   "))
    print()
    return InputPassL

def Checker(InputPassL):
    #kakailanganin mamaya tong dalawang list
    NumberList = [0,1,2,3,4,5,6,7,8,9]
    SpecialCharList = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "{", "[", "}", "]", "\\", "|", ";", ":", "'",  '"', "<", ",", ">", ".", "/", "?"]
   
    #validity checker, nasa baba ung definition nung func nila
    ValiditySpace = CriteriaSpace(InputPassL)
    Valid1ity16Letters = CriteriaA(InputPassL)
    ValidityCapital = CriteriaB(InputPassL)
    ValidityNum = CriteriaC(InputPassL, NumberList)
    ValiditySpecial = CriteriaD(InputPassL, SpecialCharList)

    #error message para alam ni user kung anong kailangan baguhin
    if ValiditySpace != "Valid":
        print(" - No spaces!")
    if Valid1ity16Letters != "Valid":
        print(" - At LEAST 16 characters!")
    if ValidityCapital != "Valid":
        print(" - At LEAST 1 capital letter!")
    if ValidityNum != "Valid":
        print(" - At LEAST 1 number!")
    if ValiditySpecial != "Valid":
        print(" - At LEAST 1 special character!")   

    #loop hanggang makapagbigay ng password na magsasatisfy sa lahat ng conditions
    while  ValiditySpace != "Valid" or Valid1ity16Letters != "Valid" or ValidityCapital != "Valid" or  ValidityNum != "Valid" or ValiditySpecial != "Valid":
        print("\nTry Again!")
        InputPassL = AskInput()
        ValiditySpace, Valid1ity16Letters, ValidityCapital,  ValidityNum, ValiditySpecial = Checker(InputPassL)
        return ValiditySpace, Valid1ity16Letters, ValidityCapital,  ValidityNum, ValiditySpecial
    return ValiditySpace, Valid1ity16Letters, ValidityCapital,  ValidityNum, ValiditySpecial

def CriteriaSpace(InputPassL):
    #Additional criteria ko lng - No Spaces allowed
    SpaceCounter = 0
    for character in InputPassL:
        if character == " ":
            SpaceCounter = SpaceCounter + 1
    if SpaceCounter == 0:
        ConditionSpace = "Valid"
        return ConditionSpace

def CriteriaA(InputPassL):
    #Criteria A - more than 15 characters
     if len(InputPassL) > 15:
        ConditionA = "Valid"
        return ConditionA

def CriteriaB(InputPassL):
    #Criteria B - At least 1 capital letter
        UpperCaseCounter = 0
        for character in InputPassL:
            if character.isupper():                                 # .isupper() checks if all character in a string is uppercase
                UpperCaseCounter = UpperCaseCounter + 1
        if UpperCaseCounter > 0:
            ConditionB = "Valid"
            return ConditionB   

def CriteriaC(InputPassL, NumberList):
    #Criteria C - At least 1 number
        NumberCounter = 0
        for character in InputPassL:
            if character in str(NumberList):                        #str ung numberlist since integer sya nung natype sa taas kanina
                NumberCounter = NumberCounter + 1
        if NumberCounter > 0:
            ConditionC = "Valid"
            return ConditionC

def CriteriaD(InputPassL, SpecialCharList):
    #Criteria D - At least 1 special char
        SpecialCharCounter = 0
        for character in InputPassL:
            if character in SpecialCharList:
                SpecialCharCounter = SpecialCharCounter + 1
        if SpecialCharCounter > 0:
            ConditionD = "Valid"
            return ConditionD

def Display():                 #Hindi aabot rito hanggat d nagiging valid
    print("\nVALID! Thank you! Your password is now STRONG and SECURED!\n") 


if __name__ == "__main__":

    #1 Ask for password input
    print("\nHey, Register a VALID password to your account.")
    print("VALID password must be:\n  a. Greater than 15 letters,\n  b. Have at least one capital letter,\n  c. Have at least one number,\n  d. And have at least one special character")
    InputPass = AskInput()

    #2 Check for validity, ask again if invalid
    Checker(InputPass)

    #3 Display 
    Display()
  