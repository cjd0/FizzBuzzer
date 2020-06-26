print("Welcome to the FizzBuzzer. Traditionally FizzBuzz is played by counting up from 1 and replacing every multiple of 3 with 'Fizz', " +
"every multiple of 5 with 'Buzz' and every multiple of both with 'FizzBuzz'. The FizzBuzzer allows you to create a custom version of this " +
"game in which you can replace 'Fizz', 'Buzz', 3, and 5 with words and numbers of your choice and increment by a specified amount across a " + 
"defined range. Let's begin...")

#method to prevent outputting floats such as 12.0
def formatNum(num):
    if num % 1 == 0:
        return int(num)
    else:
        return num

#initialise empty list and ask for all necessary string inputs
#TODO: add data validation to rangeMin, rangeMax, firstNum and secondNum
resultList = []
rangeMin = float(input("Choose first number in range: "))
rangeMax = float(input("Choose last number in range: "))
firstWord = input("Choose first word: ")
secondWord = input("Choose second word: ")
incAmount = float(input("Choose increment amount: "))
firstNum = float(input("Choose first divisor: "))
secondNum = float(input("Choose second divisor: "))

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