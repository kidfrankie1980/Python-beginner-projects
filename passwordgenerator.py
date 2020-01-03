#Password Generator
#Write a programme, which generates a random password for the user. 
#Ask the user how long they want their password to be, and how many letters and numbers they want in their password. 
#Have a mix of upper and lowercase letters, as well as numbers and symbols. 
#The password should be a minimum of 6 characters long.

import random
import string

# Function to ask for length of password
def ask_user_length():
	length = input('Select length of Password\nMinimum of 6 characters: \n').strip()

	try:
		if int(length) < 6:
			print('Password too short. Minimum 6 Characters')
			return ask_user_length()
		else:
			return int(length)
	except ValueError:
		print('Not a number. Select a Number')
		return ask_user_length()

# Function to ask for number of numbers in password
def ask_user_number():
	noofno = input('Select number of numbers in password:\nNote: the remaining characters will be letters\n').strip()
	
	try:
		if int(noofno) > plength:
			print('selected number is larger than password')
			return ask_user_number()
		else:
			return int(noofno)
	except ValueError:
		print('Not a number. Select a Number')
		return ask_user_number()

# Function to return number of letters
def ask_user_letter():
	return int(plength - pnoofno)

#Main program
plength = ask_user_length()
pnoofno = ask_user_number()
pnoofletter = ask_user_letter()

# Create empty arrays
numberarray = [0]*pnoofno
letterarray = [None]*pnoofletter

# Randomise numbers into array over request length
i=0
while i < pnoofno:
	numberarray[i] = random.randint(0,9)
	i += 1

# Randomise all printable characters into array
i=0
while i < pnoofletter:
	letterarray[i] = random.choice(string.printable)
	i += 1

# Join arrays and shuffle
passarray= numberarray + letterarray
random.shuffle(passarray)

# Write array into string.
password = ''.join([str(item) for item in passarray ])

print('You password is:', password)
