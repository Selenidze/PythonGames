with open('C:/Users/Pavel/Documents/My Code/PythonGames/remove_unwanted/remove_unwanted.py') as f:
    lines = f.read().splitlines()

#print(lines)
print(*lines, sep = "\n")