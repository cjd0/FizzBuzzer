#method to prevent outputting floats such as 12.0
def formatNum(num):
    if num % 1 == 0:
        return int(num)
    else:
        return num

#method to validate user inputs for numbers
def validateNum(message):
    valid = False
    userInput = ""
    while not valid:
        try:
            userInput = float(input(message))
        except ValueError:
            print("Please enter a number.")
        else:
            return userInput
            valid = True

#
# MAIN CODE
#

print("Welcome to the FizzBuzzer. Traditionally FizzBuzz is played by counting up from 1 and replacing every multiple of 3 with 'Fizz', " +
"every multiple of 5 with 'Buzz' and every multiple of both with 'FizzBuzz'. The FizzBuzzer allows you to create a custom version of this " +
"game in which you can replace 'Fizz', 'Buzz', 3, and 5 with words and numbers of your choice and increment by a specified amount across a " + 
"defined range. Let's begin...")

#initialise empty list and ask for all necessary string inputs
#TODO: choose whether you increment up or down first and add appropriate validation to rangeMin, rangeMax and increment
resultList = []
maxLoop = False
rangeMin = validateNum("Choose first number in range: ")
while not maxLoop:
    rangeMax = validateNum("Choose last number in range: ")
    if rangeMax <= rangeMin:
        print("Please choose a number higher than the first number.")
    else:
        maxLoop = True
firstWord = input("Choose first word: ")
secondWord = input("Choose second word: ")
incAmount = validateNum("Choose increment amount: ")
firstNum = validateNum("Choose first divisor: ")
secondNum = validateNum("Choose second divisor: ")

#loop to check each number against divisors and append appropriate value to list
while rangeMin <= rangeMax:
    if (rangeMin % firstNum == 0) and (rangeMin % secondNum == 0):
        resultList.append(firstWord + secondWord)
    elif rangeMin % firstNum == 0:
        resultList.append(firstWord)
    elif rangeMin % secondNum == 0:
        resultList.append(secondWord)
    else:
        resultList.append(str(formatNum(round(rangeMin, 2))))
    rangeMin = rangeMin + incAmount

#FizzBuzz replaced with chosen words
print("Here is your customised " + firstWord + secondWord + ":")
#print the finished list with each element separated by commas
print(*resultList, sep = ", ")