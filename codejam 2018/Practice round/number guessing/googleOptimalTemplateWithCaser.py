itIsTheFirstLine = True     #This variable is about the input line. If the line is the first the variable itIsTheFirstLine is True.
T=0     #The number of lines with usefull Data. the number of tierations.
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




def guessNumber(answerFromTheSystem):
    if answerFromTheSystem == "TOO_SMALL":
        print("the number is too small")
    elif answerFromTheSystem == "TOO_BIG":
        print("the number is too big")
    elif answerFromTheSystem == "CORRECT":
        print("that is the correct number")
    else:
        print("Something is wrong")


while (working == True):
    if itIsTheFirstLine == True:
        fileForInput = input("feed me with the first input")
        T = fileForInput
        itIsTheFirstLine = False
        print("it is the first line")
    else:
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

