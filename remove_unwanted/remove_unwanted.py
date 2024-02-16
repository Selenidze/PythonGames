# This script removes unwanted elements from source code
import re                               # A library for regex

# Configuration
TEXTTOSEARCH = [ 
    '^\\s+',                            # Line starts with one or more spaces
    '^(?!\\d+\\.)',                     # Line doesn't start with a digits with following '.' (e.g., 12.)
    '^\\d+\\.\\s?',                     # Line starts with one or more digits following a period and zero or one space
]

TEXTTOREPLACE= [
    '',                                 # Nothing
    ' ',                                # Space
]

def delSequence (listOfStrings, textToSearch, textToReplace):
    listIndex = 0

    for line in listOfStrings:
        listOfStrings[listIndex] = re.sub(textToSearch, textToReplace, line)
        listIndex += 1

def joinStrings(listOfStrings, textToSearch, textToReplace):
    listIndex = len(listOfStrings) - 1

    for line in reversed(listOfStrings):
        if re.match(textToSearch, line):
            listOfStrings[listIndex-1 : listIndex+1] = [textToReplace.join(listOfStrings[listIndex-1 : listIndex+1])]
        listIndex -= 1

def main(textToSearch, textToReplace):
    print("File to perform Search-Replace on:")
    fileToChange = input("--> ")

    with open(fileToChange) as fileTR:
        listOfStrings = fileTR.read().splitlines()

    delSequence(listOfStrings, textToSearch[0], textToReplace[0])                       # Removing spaces at the beginning of lines
    joinStrings(listOfStrings, textToSearch[1], textToReplace[1])                       # Joining strings not starting with a digit 
    delSequence(listOfStrings, textToSearch[2], textToReplace[0])                       # Removing numbers of lines

    #print(*listOfStrings, sep = "\n")                                                  # Printing the list

    with open(fileToChange, 'w') as fileTW:
        for line in listOfStrings[:-1]:
           fileTW.write('%s\n' % line)                                                  # Write each element add \n at the end
        fileTW.write('%s' % listOfStrings[-1])                                          # Don't add \n at the end of the last line

    input('\n\nPress Enter to exit...')

if __name__ == "__main__": 
    main(TEXTTOSEARCH, TEXTTOREPLACE)