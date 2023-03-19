
import string
import operator
import os

#DSC 510
#Week 9
#Programming Assignment Week 9
#Author Felipe Castillo
#5/07/2021

#Change#:2
#Change(s) Made:

'''
our program must have a header. 
Create a new function called process_fie. This function will perform the same operations as pretty_print from week 8 however it will print to a file instead of to the screen.
Modify your main method to print the length of the dictionary to the file as opposed to the screen.
This will require that you open the file twice. Once in main and once in process_file.
Prompt the user for the filename they wish to use to generate the report.
Use the filename specified by the user to write the file.
This will require you to pass the file as an additional parameter to your new process_file function.
'''

finalAdjTextList = [] #After program is processed accessable by main
d_gettysburg = dict()

def process_file(d_gettysburg_processed, savedFileName):
    word = 'word'
    count = 'count'
    sorted_d = dict(sorted(d_gettysburg_processed.items(),key=operator.itemgetter(1), reverse= True)) # sort program in order

    try:
        cwd = os.getcwd() # gets current path regardless of users
        file = open(cwd + "\\"+ savedFileName+".txt", 'w')

        header = ("Length of dictionary:  "
                  "" + len(sorted_d).__str__() + "\n"
                    + f"{word:12}           {count:10}"
                    +"\n----------------------------\n")

        file.write(header)
        for key , value in sorted_d.items():
            file.write(f'{key:12}     {value:10d} \n')
        file.close()
    except:
        print("Couldn't write to file.")


def add_word(wordsList):

    for i in wordsList:
        if i in d_gettysburg:
            d_gettysburg[i] = d_gettysburg[i] + 1
        else:
             d_gettysburg[i] = 1


def process_line(lines):

    sentence = ''.join(lines)# independent 4 line array combined into a single string
    wordsList = []
    word_lowered = sentence.lower()
    words = word_lowered.split()
    for i in words:
        words_withoutPunctuation = i.translate(i.maketrans("", "", string.punctuation))# removes all punctuations like , -- .
        wordsList.append(words_withoutPunctuation)
    if len(wordsList) > 0:
        finalAdjText = list(filter(None, wordsList))  # take out the left over blanks
        for j in finalAdjText:
            finalAdjTextList.append(j)#final adjusted list keys and values

def main():
    listArrayBeforeChanges = []

    while True:

        saved_toFile_name = input("What would you like to name your file?")

        if(saved_toFile_name != ""):
            try:
                gettysburg_file = open('gettysburg.txt', 'r')
                for line in gettysburg_file:
                    listArrayBeforeChanges.append(line)
                if len(listArrayBeforeChanges) > 0:
                    process_line(listArrayBeforeChanges)
                else:
                    ("No data was processed")

                if len(finalAdjTextList) > 0:
                    add_word(finalAdjTextList)
                    process_file(d_gettysburg, saved_toFile_name)
                    print("Process was sucessful.")
                    break
                else:
                    print("Error has occured no words were found in the file, please look inside the file and try again") # if  note pad is empty there are no words, list is empty
                    break
            except:
                print("couldnt open file, please check the name of the file your getting data from and try again.")
                break
        else:
            print("Please insert a file to save no updated changes.")

if __name__ == '__main__':
    main()







