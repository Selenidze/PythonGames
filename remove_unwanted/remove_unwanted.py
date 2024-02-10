import re

#import os
#import sys
import fileinput

def editTextInFile(text_to_search, replacement_text, filename, eol):
    with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
        for line in file:
            #replacement_text = line
            #print(line.replace(text_to_search, replacement_text), end='')
            #replacement_text = '!' + re.search(text_to_search, line) + '!'
            #print(re.search(text_to_search, line))
            print(re.sub(text_to_search, replacement_text, line), end=eol)

def FindTextInFile(text_to_search, replacement_text, filename, eol):
    with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
        for line in file:
            #replacement_text = line
            #print(line.replace(text_to_search, replacement_text), end='')
            #replacement_text = '!' + re.search(text_to_search, line) + '!'
            #print(re.search(text_to_search, line))
            print(re.sub(text_to_search, replacement_text, line), end=eol)

def editTextInFile2(textToSearch, textToReplace, fileToSearch, eol):
    tempFile = open(fileToSearch, 'r+')

    counter = 1
    for line in fileinput.input(fileToSearch):
        if textToSearch in line:
            print('Match Found')
        else:
            print('Match Not Found!!')

        print(counter, end=': ')
        print(re.search(textToSearch, line))
        test = re.match(textToSearch, line)
        print(test)
        #tempFile.write(line.replace(textToSearch, textToReplace))
        tempFile.write(re.sub(textToSearch, textToReplace, line))
        counter += 1
    tempFile.close()

def main():
    #print("Text to search for:")
    #textToSearch = input("--> ")
    textToSearch2 = '(\\s)?(\\d)+\\.(\\s)?' 
    #textToSearch1 = '(\\s)?(\\d)+\\.(\\s){1}'
    textToSearch1 = '(\\s)?(\\d)+\\.\\n'
    textToSearch0 = '^(?!((\\s)?(\\d)+\\.)).+'

    #print("Text to replace it with:")
    #textToReplace = input("--> ")
    textToReplace0 = 'FUNNY'
    textToReplace1 = '\n'
    textToReplace2 = ''

    #print("File to perform Search-Replace on:")
    #fileToSearch = input("--> ")
    fileToSearch = 'c:/Users/Pavel/Documents/My Code/PythonGames/remove_unwanted/pre_dragon.py'

    endOfLine = ''

    editTextInFile2(textToSearch0, textToReplace0, fileToSearch, endOfLine)

    #editTextInFile(textToSearch1, textToReplace1, fileToSearch, endOfLine)
    #editTextInFile(textToSearch2, textToReplace2, fileToSearch, endOfLine)

#    input('\n\n Press Enter to exit...')

if __name__ == "__main__": 
    main()