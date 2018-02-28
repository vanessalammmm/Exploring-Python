# Guess a random number!

import random

correctnumber=random.randint(0, 20)

print('I am thinking of a number between 0 and 20. Guess what is is!')
myguess=int(input())

while myguess < correctnumber:
	print('Hmmm too low, try again!')
	myguess=int(input())

while myguess > correctnumber:
	print('That's too high, guess again!')
	myguess=int(input())

if myguess==correctnumber:
	print('You guessed it!')
