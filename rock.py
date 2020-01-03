#Rock, Paper, Scissors Game
#Make a rock-paper-scissors game where it is the player vs the computer. 
#The computer’s answer will be randomly generated, while the program will ask the user #for their input. 
#This project will better your understanding of while loops and if statements.

import random
import time

#function for correct inputs.
def ask_user():
	humaninput = input('Choose Rock, Paper or Scissors??: \n').strip().lower()
	
	if humaninput == 'rock':
		return 'rock'
	elif humaninput == 'paper':
		return 'paper'
	elif humaninput == 'scissors':
		return 'scissors'
	else:
		print('invailed guess. try again')
		return ask_user()

#function to ask the player to play again.
def playagain():
	user= input('Do you want to play again?: Y or N: \n').strip().lower()

	if user == 'y':
		return True
	elif user == 'n':
		return False
	else:
		print('invailed guess. try again')
		return playagain()

#when game starts the player wants to play the game.
playgame = True

while playgame != False:
	
	#this is the computers choice
	hands = ['rock', 'paper', 'scissors']
	strcompguess = random.choice(hands)

	#human input for rock / paper / scissors
	humanguess = ask_user()
	
	#logic to determine winner with one second p
	if humanguess == strcompguess:
		print('draw')
	elif humanguess == 'rock' and strcompguess == 'paper':
		print('You lose. Computer chose paper')
	elif humanguess == 'paper' and strcompguess == 'scissors':
		print('You lose. Computer chose scissors')
	elif humanguess == 'scissors' and strcompguess == 'rock':
		print('You lose. Computer chose rock')
	elif humanguess == 'paper' and strcompguess == 'rock':
		print('You Win. Computer chose rock')
	elif humanguess == 'rock' and strcompguess == 'scissors':
		print('You Win. Computer chose scissors')
	elif humanguess == 'scissors' and strcompguess == 'paper':
		print('You Win. Computer chose paper')
		
	time.sleep(0.5)
	playgame = playagain()