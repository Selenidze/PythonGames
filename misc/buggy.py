import random
number1 = random.randint(1, 10)
number2 = random.randint(1, 10)
print('What is ' + str(number1) + ' + ' + str(number2) + '?')
answer = input()
if answer == number1 + number2:
#if int(answer) == number1 + number2: # Here is the correction
else:
    print('Nope! The answer is ' + str(number1 + number2))