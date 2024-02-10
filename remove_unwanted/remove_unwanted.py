# This script removes numbers of lines from source code
import re                               # A library for regex
import fileinput                        # A library for work with files

# Configuration
textToSearchArray = [ 
    '(\\s)*(\\d)+\\.\\n',               # Only a number of line
    '(\\s)*(\\d)+\\.(\\s)?',            # A number of line and a text
]

textToReplaceArray = [
    '\n',                               # A new line instead a number of line
    '',                                 # Just replace without a new line
]

endOfLineArray = [
    '',                                 # Not add a new line
]

def editTextInFile(search, replace, filename, eol):
    with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
        for line in file:
            print(re.sub(search, replace, line), end=eol)

def main(textToSearch, textToReplace, endOfLine):
      
    print("File to perform Search-Replace on:")
    fileToSearch = input("--> ")

    editTextInFile(textToSearch[0], textToReplace[0], fileToSearch, endOfLine[0])
    editTextInFile(textToSearch[1], textToReplace[1], fileToSearch, endOfLine[0])

    input('\n\nPress Enter to exit...')

if __name__ == "__main__": 
    main(textToSearchArray, textToReplaceArray, endOfLineArray)