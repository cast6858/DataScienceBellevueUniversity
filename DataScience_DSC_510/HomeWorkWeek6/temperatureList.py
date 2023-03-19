
#DSC 510
#Week 6
#Programming Assignment Week 6
#Author Felipe Castillo
#4/19/2021

#Change#:1
#Change(s) Made:
'''

Your program must have a header.
Create an empty list called temperatures.
Allow the user to input a series of temperatures along with a sentinel value (do not use a number for a sentinel value) which will stop the user input.
Evaluate the temperature list to determine the largest and smallest temperature.
Print the largest temperature.
Print the smallest temperature.
Print a message that tells the user how many temperatures are in the list.

'''

#Date of Change: 04/19/2021
#Author: Felipe Castillo


def temperature_validation(amountOfTemps): # setting an error code to 001 , temp can be zero high or lower
    relisticTemp = ''
    if amountOfTemps > 150: #hottest temp record was 137 degress anything else error 001 is an error
        relisticTemp = '001'
    elif int(amountOfTemps) < int(-200): # coldest place recorded was 187 anything else error 001 is an error
        relisticTemp = '001'
    else:
        relisticTemp = str(amountOfTemps)
    return relisticTemp

def min_max_temperature(temperatures):
    if (temperatures != 0 or temperatures != ""):
        low = temperatures[0]
        high = temperatures[0]
        for temp in temperatures:
            if (temp >  low):
                low = temp
            elif (temp < high):
                high = temp
        return low, high
    else:
        print("You must provide at least one number")

def temperature_calculations():
    temperatures = [] #storing temps
    amountTemperatures = input("Enter the amount of tempertures you want to insert")
    if (not amountTemperatures.isnumeric()):
        amountTemperatures = None
        print("You inserted a none number please re run the program")
    elif(int(amountTemperatures) == 0):
        print("Please insert a number above 0 re run program")
        amountTemperatures = None
    else:
        amountTemperatures = int(amountTemperatures)

    if(amountTemperatures != None):
        while amountTemperatures > 0:
            temperatures_numbers = input("Insert your tempertures: ")
            if (temperatures_numbers.isnumeric() or temperatures_numbers.strip('-').isnumeric()):
                validatedTemperature = temperature_validation(int(temperatures_numbers))
                if(validatedTemperature != "001"):
                    temperatures.append(int(validatedTemperature))
                    amountTemperatures = amountTemperatures - 1
                else:
                    print("Please insert a realistic temperature hint hottest is 150 coldest -187")
            else:
                print("Ooops try inserting a number")

        tempReturned = min_max_temperature(temperatures) # returns a tuple with high and low
        highTemperature = str(tempReturned).split(",")[0].replace("(", "").strip()
        lowTemperature = str(tempReturned).split(",")[1].replace(")", "").strip()

        print("\nThere are "+  len(temperatures).__str__() + " temperatures in the list.")
        print("The highest temperature is " + highTemperature+ "°F")
        print("The lowest temperature is " + lowTemperature+ "°F\n")


   # print(max(temperatures))   function to find max
   # print(min(temperatures)) function to find min

def main():
    while True:
        temperatureSimulation = input("Would you like to run the temperature simulation  (1) YES , (0) NO")
        if (temperatureSimulation == '1' or temperatureSimulation== "YES"):
            temperature_calculations()
        elif (temperatureSimulation == '0' or temperatureSimulation == "NO"):
            print("Thank you for your interest in temperature simulation")
            break
        else:
            print("Oooop inset vaild key 0 for no or 1 for yes")

if __name__ == '__main__':
    main()