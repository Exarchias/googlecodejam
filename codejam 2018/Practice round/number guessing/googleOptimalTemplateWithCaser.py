import random

itIsTheFirstLine = True     #This variable is about the input line. If the line is the first the variable itIsTheFirstLine is True.
T=0     #The number of lines with usefull Data. the number of tierations.
theRangeArray = []
A=""
B=""
newA=0
newN=0
lastNumber=0
lastMAX=0
lastMIN=0
result = "Not any result right now" #this is used for the result wich is printed in the end of the code with the default value.
testSum = 0 #This is used to make the mainCheckFunction() bit more interesting but making the function to work as add function.
countForT = 0 #this is the count vairiable that helps to check that the iterations are not more than the predefined T variable.
countForDwnldN = 0
dwnldK = 0
caserArray = []
i = 0
working = True
#fileForOutput = open('output.txt','w')
#fileForInput = open('input.in','r')
#fileForInput = input("feed me with input")


def setNewMax(newMAX, oldMAX):
    if int(newMAX) < int(oldMAX):
        print("The newmax is smaller than oldmax so I will return newmax")
        print("Newmax=", newMAX, " OldMAX=", oldMAX)
        return newMAX
    else:
        print("The newmax is bigger than oldmax so I will return oldmax")
        print("Newmax=", newMAX, " OldMAX=", oldMAX)
        return oldMAX


def setNewMin(newMIN, oldMIN):
    if int(newMIN) > int(oldMIN):
        print("The newmin is bigger than oldmin so I will return newmin")
        print("Newmax=", newMIN, " OldMAX=", oldMIN)
        return newMIN
    else:
        print("The newmin is smaller than oldmin so I will return oldmin")
        print("Newmin=", newMIN, " OldMIN=", oldMIN)
        return oldMIN


def guessNumber(answerFromTheSystem):
    global i, newA, newB, lastNumber, lastMAX, lastMIN
    if answerFromTheSystem == "TOO_SMALL":
        print("the number is too small")
        lastMIN = setNewMin(lastNumber, lastMIN)
        lastNumber = smallGuess(lastMIN, lastMAX)
        print("I recommend", lastNumber)
    elif answerFromTheSystem == "TOO_BIG":
        print("the number is too big")
        lastMAX = setNewMax(lastNumber, lastMAX)
        lastNumber = bigGuess(lastMIN, lastMAX)
        print("I recommend", lastNumber)
    elif answerFromTheSystem == "CORRECT":
        print("that is the correct number")
        newA = 0
        newB = 0
        i = int(T)
    else:
        print("Something is wrong")


def firstGuess(A,B):
    theNumber = random.randrange(int(A), int(B), 1)
    print("I am doing a firstGuess. MIN is ", A, " and MAX is", B)
    return str(theNumber)

def smallGuess(A,B):
    theNumber = random.randrange(int(A)+1, int(B), 1)
    print("I am doing a smallGuess. MIN is ", A, " and MAX is", B)
    return str(theNumber)

def bigGuess(A,B):
    theNumber = random.randrange(int(A), int(B)-1, 1)
    print("I am doing a bigGuess. MIN is ", A, " and MAX is", B)
    return str(theNumber)





while (working == True):
    if itIsTheFirstLine == True:
        fileForInput = input("feed me with the first input")
        T = fileForInput
        itIsTheFirstLine = False
        print("it is the first line")
    else:
        theRange = input("define the range [A B]")
        theRangeArray = theRange.split()
        A = theRangeArray[0]
        B = theRangeArray[1]
        newA = theRangeArray[0]
        newB = theRangeArray[1]
        print("The theRangeArray is", theRangeArray)
        print("The range is", theRange)
        print("The A is", A)
        print("The B is", B)
        theFirstChoosenNumber = firstGuess(A,B)
        lastNumber = theFirstChoosenNumber
        lastMAX = B
        lastMIN = A
        print("The first choosen number is", theFirstChoosenNumber)

        print("Now we check the cases")
        while i < int(T):
            fileForInput = input("give the second input input")
            guessNumber(fileForInput)
            print("guess the number funktion. i is", str(i+1), "and T is", T)
            print("guess the number funktion. isthefirstline is", itIsTheFirstLine)
            i = i + 1
        else:
            print("we passed the limit")
            print("ELSE. i is", i, "and T is", T)
            print("ELSE. isthefirstline is", itIsTheFirstLine)
            i=0
            itIsTheFirstLine = True
            print("ELSE. i is", i, "and T is", T)
            print("ELSE. isthefirstline is", itIsTheFirstLine)



#fileForOutput.close()
print("That's all folks!")

