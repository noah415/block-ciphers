import sys
import os
import cryptography
from ciphers.cbc import cbc
from ciphers.ecb import ecb

task_one_prompt = '1) encrypt a file'
task_two_prompt = '2) mimic a website'
exit_prompt = '4) exit'

def main():

	while True:
		user_choice = input(f'\nSelect an option:\n\n{task_one_prompt}\n{task_two_prompt}\n{exit_prompt}\n> ')

		if not user_choice.isnumeric() or int(user_choice) <= 0 or int(user_choice) > 4:
			print('\nPlease enter a valid number for your choice.')

		else:

			if int(user_choice) == 1:
				task_one()
				continue

			if int(user_choice) == 2:
				pass

			if int(user_choice) == 3:
				pass

			if int(user_choice) == 4:
				break

	return

def task_one():

	if 'outputs' not in os.listdir():
		os.mkdir('outputs')

	if not os.path.isdir('outputs'):
		print("\nError - \'outputs\' must be a directory for file encryption")
		return

	args = input("\nUsage: <ecb | cbc> <infile> <outfile>\n\nEnter your parameters > ").split()
	if len(args) != 3:
		print("Usage: <ecb | cbc> <infile> <outfile>")
		return
	
	if args[0].lower() not in ['ecb', 'cbc']:
		print(f'You chose to incrypt using "{args[0]}" but the only valid modes are ecb or cbc.')
		return

	mode = args[0].lower()
	infile = args[1]
	outfile = args[2]

	if mode == 'ecb':
		ecb(infile, outfile)
	if mode == 'cbc':
		cbc(infile, outfile)
	return None

if __name__ == '__main__':
	main()