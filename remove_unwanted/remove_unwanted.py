# This script removes unwanted elements from source code
import re                               # A library for regex

# Configuration
TEXTTOSEARCH = [ 
    '^\\s+',                            # Line starts with one or more spaces
    '^\\D',                             # Line doesn't start with a digit
    '^\\d+\\.\\s?',                     # Line starts with one or more digits following a period and zero or one space
]

TEXTTOREPLACE= [
    '',                                 # Nothing
    ' ',                                # Space
]

def delSequence (listOfStrings, textToSearch, textToReplace):
    listOfStrings = [re.sub(textToSearch, textToReplace, line) for line in listOfStrings]  
    return listOfStrings

def joinStrings(listOfStrings, textToSearch, textToReplace):
    listIndex = len(listOfStrings) - 1

    for line in reversed(listOfStrings):
        if re.match(textToSearch, line):
            #print(str(listIndex) + '(CHANGE): ' + textToReplace.join(listOfStrings[listIndex-1 : listIndex+1]))
            listOfStrings[listIndex-1 : listIndex+1] = [textToReplace.join(listOfStrings[listIndex-1 : listIndex+1])]
       # else:
           # print(str(listIndex) + ': ' + line)
        listIndex -= 1

    return listOfStrings

def main(textToSearch, textToReplace):
    print("File to perform Search-Replace on:")
    fileToChange = input("--> ")

    with open(fileToChange) as fileTR:
        listOfStrings = fileTR.read().splitlines()

    listOfStrings = delSequence(listOfStrings, TEXTTOSEARCH[0], TEXTTOREPLACE[0])       # Removing spaces at the beginning of lines
    listOfStrings = joinStrings(listOfStrings, TEXTTOSEARCH[1], TEXTTOREPLACE[1])       # Joining strings not starting with a digit 
    listOfStrings = delSequence(listOfStrings, TEXTTOSEARCH[2], TEXTTOREPLACE[0])       # Removing numbers of lines

    #print(*listOfStrings, sep = "\n")                                                  # Printing the list

    with open(fileToChange, 'w') as fileTW:
        for line in listOfStrings:
           fileTW.write('%s\n' % line)                                                  # Write each item on a new line

    input('\n\nPress Enter to exit...')

if __name__ == "__main__": 
    main(TEXTTOSEARCH, TEXTTOREPLACE)