#Guess The Number 
#Write a programme where the computer randomly generates a 
#number between 0 and 20. The user needs to guess what the 
#number is. If the user guesses wrong, tell them their guess 
#is either too high, or too low. This will get you started 
#with the random library if you haven't already used it.

import random
import time

#This function ask to play again Y or No
def playagain():
	user= input('Do you want to play again?: Y or N: \n').strip().lower()

	if user == 'y':
		return True
	elif user == 'n':
		return False
	else:
		print('invailed guess. try again')
		return playagain()

guess = ''
playgame = True

while playgame != False:
	starttime= time.time()
	solution = random.randrange(0,20,1)
	print(solution)
	
	while guess != solution:
		try:	
			guess = int(input('Please Enter a number between 0 - 20: \n'))
		except ValueError:
			print ("Not a number. Try again!")
			continue

		if guess < solution:
			print('Your guess is too low')
		if guess > solution:
			print('Your guess is too high')		


		if int(guess) == solution:
			break
	
	print('Correct! The solution was:  ' + str(solution))
	print('Completed in %s' % (time.time() - starttime))

	playgame = playagain()









