
from CashRegister import Cash_Register
import locale


#DSC 510
#Week 11
#Programming Assignment Week 11
#Author Felipe Castillo
#5/27/2021

#Change#:1
#Change(s) Made:

'''
Your program must have a header.
Your program must have a welcome message for the user.
Your program must have one class called CashRegister.
Your program will have an instance method called addItem which takes one parameter for price. The method should also keep track of the number of items in your cart.
Your program should have two getter methods.
getTotal – returns totalPrice
getCount – returns the itemCount of the cart
Your program must create an instance of the CashRegister class.
Your program should have a loop which allows the user to continue to add items to the cart until they request to quit.
Your program should print the total number of items in the cart.
Your program should print the total $ amount of the cart.
The output should be formatted as currency. Be sure to investigate the locale class. You will need to call locale.setlocale and locale.currency.

'''

def print_cart_items(cashRegister):
    if(cashRegister.get_total() > 0):
        locale.setlocale(locale.LC_ALL, 'en_SG')

        print("You have " + cashRegister.get_count().__str__() + " in your cart")
        print("Total price for items " + locale.currency(cashRegister.get_total(), grouping=True))

    else:
        print("No items were registered, thank you")


def establish_cart():
    run = True
    cashRegister = Cash_Register()


    while run:
        const_price = input("insert price or Q to quit")
        if (const_price.isnumeric() or const_price.replace(".","").isdigit()): # check for float and int
            cashRegister.add_item(float(const_price))
        elif(const_price == 'Q' or const_price == 'q'):
            run = False
        else:
            print("Not a valid key please try again")

    print_cart_items(cashRegister)


def main():
    print("Welcome to cash register.")

    while True:
        answer = input("Do you want to run program: (Y) Yes or (N) No.")
        if (answer == 'Y' or answer == 'y'):
            establish_cart()
            break
        elif(answer == 'N' or answer == 'n'):
            print("Thank you for using this program.")
            exit()
        else:
            print("Invalid key way in try again")

if __name__ == '__main__':
    main()


