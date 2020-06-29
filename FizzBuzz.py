import operator

#method to output integers without the trailing '.0'
def formatNum(num):
    if num % 1 == 0:
        return int(num)
    else:
        return num

#method to validate user inputs for numbers
def validateNum(message):
    inputValid = False
    userInput = ""
    while not inputValid:
        try:
            userInput = float(input(message))
        except ValueError:
            print("Please enter a number.")
        else:
            return userInput
            inputValid = True

#method to validate end value and define whether the code is to increment or decrement
def validateEnd(rStart):
    #global keyword used to change value of direction boolean
    global direction
    maxLoop = False
    while not maxLoop:
        rEnd = validateNum("Choose end number in range. Choose a higher number to count up and a lower number to count down: ")
        if rEnd == rStart:
            print("Please choose a number higher or lower than the first number.")
        elif rEnd < rStart:
            direction = False
            maxLoop = True
            return rEnd
        else:
            maxLoop = True
            return rEnd

#method to validate the increment value and modify the output according to the value of the direction boolean
def validateInc(dir):
    incLoop = True
    inc = 0
    while incLoop:
        if dir:
            inc = validateNum("Choose increment amount: ")
            if inc <= 0:
                print("Please choose a positive number.")
            else:
                return inc
        else:
            inc = validateNum("Choose decrement amount: ")
            if inc >= 0:
                print("Please choose a negative number.")
            else:
                return inc

#method to build the 'FizzBuzz' in the empty list, the argument is to pass the <= or >= operator dependent on the value of the direction boolean
def buildList(op, rangeStart,rangeEnd):
    while op(rangeStart, rangeEnd):
        if (rangeStart % firstNum == 0) and (rangeStart % secondNum == 0):
            resultList.append(firstWord + secondWord)
        elif rangeStart % firstNum == 0:
            resultList.append(firstWord)
        elif rangeStart % secondNum == 0:
            resultList.append(secondWord)
        else:
            resultList.append(str(formatNum(round(rangeStart, 2))))
        rangeStart = rangeStart + incAmount

#
# MAIN CODE
#

print("Welcome to the FizzBuzzer. Traditionally FizzBuzz is played by counting up from 1 and replacing every multiple of 3 with 'Fizz', " +
"every multiple of 5 with 'Buzz' and every multiple of both with 'FizzBuzz'. The FizzBuzzer allows you to create a custom version of this " +
"game in which you can replace 'Fizz', 'Buzz', 3, and 5 with words and numbers of your choice and increment or decrement by a specified amount " + 
"across a defined range. Let's begin...")

#initialise empty list and ask for all necessary string inputs
#TODO: choose whether you increment up or down first and add appropriate validation to rangeStart, rangeEnd and increment
resultList = []
#direction boolean - true = count up, false = count down
direction = True
rangeStart = validateNum("Choose start number in range: ")
#maxLoop and direction validation
rangeEnd = validateEnd(rangeStart)
firstWord = input("Choose first word: ")
secondWord = input("Choose second word: ")
print (direction)
#increment/decrement and validation
incAmount = validateInc(direction)
firstNum = validateNum("Choose first divisor: ")
secondNum = validateNum("Choose second divisor: ")

#uses the value of direction to pass <= or >= operators into the function argument
if direction:
    buildList(operator.le, rangeStart, rangeEnd)
else:
    buildList(operator.ge, rangeStart, rangeEnd)

#FizzBuzz replaced with chosen words
print("Here is your customised " + firstWord + secondWord + ":")
#print the finished list with each element separated by commas
print(*resultList, sep = ", ")