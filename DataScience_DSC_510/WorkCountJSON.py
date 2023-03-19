import os

'''
Open the file and process each line.
Either add each word to the dictionary with a frequency of 1 or update the word’s count by 1.
Nicely print the output, in this case from high to low frequency. You should use string formatting for this. (See discussion 8.3).
We want to achieve each major goal with a function (one function, one action). We can find four functions that need to be created.

add_word: Add each word to the dictionary. Parameters are the word and a dictionary. No return value.

Process_line: There is some work to be done to process the line: strip off various characters, split out the words,
and so on. Parameters are a line and the dictionary. It calls the function add word with each processed word. No return value.

Pretty_print: Because formatted printing can be messy and often particular to each situation (meaning that we might need
to modify it later), we separated out the printing function. The parameter is a dictionary. No return value.

main: We will use a main function as the main program. As usual, it will open the file and call process_line on each line.
 When finished, it will call pretty_print to print the dictionary.

In the main function, you will need to open the file. We will cover more regarding opening of files next week but
I wanted to provide you with the block of code you will utilize to open the file, see below.
'''
import string
import operator

finalAdjTextList = [] #After program is processed accessable by main

def pretty_print(d_gettysburg):
    word = 'word'
    count = 'count'
    sorted_d = dict(sorted(d_gettysburg.items(),key=operator.itemgetter(1), reverse= True)) # sort program in order

    print("Length of dictionary:  " + len(sorted_d).__str__())
    print(f"{word:12}           {count:10}")
    print("----------------------------")
    for key , value in sorted_d.items():
        #print(f'{name:10} ==> {phone:10d}')
        print(f'{key:12}     {value:10d}')


def add_word(wordsList):

    d_gettysburg = dict()

    for i in wordsList:
        if i in d_gettysburg:
            d_gettysburg[i] = d_gettysburg[i] + 1
        else:
             d_gettysburg[i] = 1
    pretty_print(d_gettysburg)


def process_line(lines):

    wordsList = []
    word_lowered = lines.lower()
    words = word_lowered.split()
    for i in words:
        words_withoutPunctuation = i.translate(i.maketrans("", "", string.punctuation))# removes all punctuations like , -- .
        wordsList.append(words_withoutPunctuation)
    if len(wordsList) > 0:
        finalAdjText = list(filter(None, wordsList))  # take out the left over blanks
        for j in finalAdjText:
            finalAdjTextList.append(j)


def main():
    try:
        gettysburg_file = open('gettysburg.txt', 'r')
        text = gettysburg_file.read()
        process_line(text)

        if len(finalAdjTextList) > 0:
            add_word(finalAdjTextList)
        else:
            print("Error has occured no words where found in the list")#if  note pad is empty there are no words, list is empty

    except:
        print("couldent find folder or content")


if __name__ == '__main__':
    main()

