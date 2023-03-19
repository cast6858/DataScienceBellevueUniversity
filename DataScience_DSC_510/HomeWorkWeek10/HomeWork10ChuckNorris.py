
import requests

#DSC 510
#Week 10
#Programming Assignment Week 10
#Author Felipe Castillo
#5/22/2021

#Change#:1
#Change(s) Made:

'''
Create a program which uses the Request library to make a GET request of the following API: Chuck Norris Jokes.
The program will receive a JSON response which includes various pieces of data. You should parse the JSON data to obtain the “value” key. The data associated with the value key should be displayed for the user (i.e., the joke).
Your program should allow the user to request a Chuck Norris joke as many times as they would like. You should make sure that your program does error checking at this point. If you ask the user to enter “Y” and they enter y, is that ok? Does it fail? If it fails, display a message for the user. There are other ways to handle this. Think about included string functions you might be able to call.
Your program must include a header as in previous weeks.
Your program must include a welcome message for the user.
Your program must generate “pretty” output. Simply dumping a bunch of data to the screen with no context doesn’t represent “pretty.”
'''

def joke_handler():
    url = "https://api.chucknorris.io/jokes/random"
    value = ''
    try:
        json_payload = requests.get(url).json()
        value = json_payload['value']
    except:
        value = 'Could not receive json data, check internet connection. And please try again error 001' #look for 001 for break
    return value

def main():
    print("Welcome to the Chuck Norris Joke Generator.")
    while True:
        answer = input("Do you want to hear a chuck norris Y(yes) or N(NO)")
        if(answer == 'Y' or answer == 'y'):
            joke = joke_handler()
            print(joke + "\n")
            if(joke.split(" ")[-1] == '001'): # if user click yes but error like internet is disconnect, looks for 001 error
                break
        elif(answer == 'N' or answer== 'n'):
            print("Thank your for your time come again")
            break
        else:
            print("This is an invaild entry please try again")


if __name__ == '__main__':
    main()
