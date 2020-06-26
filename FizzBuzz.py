print("Welcome to the FizzBuzzer. Traditionally FizzBuzz is played by counting up from 1 and replacing every multiple of 3 with 'Fizz', " +
"every multiple of 5 with 'Buzz' and every multiple of both with 'FizzBuzz'. The FizzBuzzer allows you to create a custom version of this " +
"game in which you can replace 'Fizz', 'Buzz', 3, and 5 with words and numbers of your choice across a defined range of integers. Let's begin...")

#initialise empty list and ask for all necessary string inputs
#TODO: add data validation to rangeMin, rangeMax, firstNum and secondNum
resultList = []
rangeMin = int(input("Choose first number in range: "))
rangeMax = int(input("Choose last number in range: "))
firstWord = input("Choose first word: ")
secondWord = input("Choose second word: ")
firstNum = int(input("Choose first divisor: "))
secondNum = int(input("Choose second divisor: "))

#loop to check each number against divisors and append appropriate value to list
for i in range(rangeMin, rangeMax + 1):
    if (i % firstNum == 0) and (i % secondNum == 0):
        resultList.append(firstWord + secondWord)
    elif i % firstNum == 0:
        resultList.append(firstWord)
    elif i % secondNum == 0:
        resultList.append(secondWord)
    else:
        resultList.append(str(i))

#FizzBuzz replaced with chosen words
print("Here is your customised " + firstWord + secondWord + ":")
#print the finished list with each element separated by commas
print(*resultList, sep = ", ")