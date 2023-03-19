#DSC 510
#Week 5
#Programming Assignment Week 5
#Author Felipe Castillo
#4/11/2021

#Change#:1
#Change(s) Made:
'''
1.Defined a function named performCalculation which takes one parameter. The parameter will be the operation being performed (+, -, *, /).
2. perform the given prompt the user for two numbers then perform the expected operation depending on the parameter that's passed into the function.
3. print the calculated value for the end user.
4.Defined a function named calculateAverage which takes no parameters.
5. ask the user how many numbers they wish to input.
6.use the number of times to run the program within a for loop in order to calculate the total and average.
7. print the calculated average.
8. main section which contains a while loop. The while loop will be used to allow the user to run the program until they enter a value which ends the loop.
9.the user for the operation they wish to perform.
10evaluate the entered data using if statements.
'''


#Date of Change: 04/11/2020
#Author: Felipe Castillo


def calculate_average():
    numberList = [] #storing numbers
    amountNumbers = input("Enter the amount of numbers your wanting to insert")
    if (not amountNumbers.isnumeric()):
        amountNumbers = 0
        print("You inserted a none number please re run the program")
    else:
        amountNumbers = int(amountNumbers)
    while amountNumbers > 0:
        number = input("Insert your numbers")
        if (number.isnumeric()):
            numberList.append(number)
            amountNumbers = amountNumbers - 1
        else:
            print("Ooops try inserting a number")
    if(numberList != ""):
        try:  # checking for division by zero error for dividing zero
            tempNumbers = 0   #intailized as a number for calculations
            for numbers in numberList:
                tempNumbers = int(tempNumbers) + int(numbers)
            average = tempNumbers / len(numberList)
            lengthOfNumberList = len(numberList)
            convertedLengthOfList = str(lengthOfNumberList)

            print("Total sum: " +str(tempNumbers)+ "\n"
                  + "Amount of numbers Insert: " + convertedLengthOfList + "\n"
                  +"Average :" +str(average))
            print(str(tempNumbers) + " / " +convertedLengthOfList + " = " + str(average))

        except ZeroDivisionError:
            print("Try inserting a vaild number above 0 ")
            print("Needs to be a number and not a word.")
    else:
        print("No numbers were returned")



def perform_calculation(operator):

    isNumber = False # Set To False Until Two Numbers are provided
    while not isNumber:
        total = ''
        numOne = input("Input the first number")
        numTwo = input("Input the second number")

        if(numOne.isnumeric() and numTwo.isnumeric() or numOne.replace(".","").isdigit() and numTwo.replace(".","").isdigit()): # Making sure its a number even if has a decimal
            try:
                total = eval(str(numOne) + "" + operator + "" + str(numTwo))
            except:
                print("oops something went wrong")
                print("exception cant divided by zero")
            return total
            break
        else:
            isNumber = False
            print("Please Try Inserting A Number")


def main():
  while True:
    operation = input("Insert operator - add(+), subtract(-), divide(/), multiple(*),  or (Q) to quit")
    if(operation == '+' or operation == '-' or operation == '/' or operation =="*"): # will not allow anything other then the operators
        total = perform_calculation(operation)
        print("Total: "+ str(total))
    elif(operation == "Q" or operation == "q"):
        break
    else:
        print("Ooops invalid key was entered")

  while True:
      runAverageCalculation = input("Would you like to add number and find averge (1) YES , (0) NO")
      if(runAverageCalculation == '1' or runAverageCalculation == "YES"):
          calculate_average()
      elif(runAverageCalculation == '0' or runAverageCalculation == "NO"):
          print("Thank you for your intrest in average calcualtor")
          break
      else:
          print("Oooop inset vaild key 0 for no or 1 for yes")


if __name__ == '__main__':
    main()
