import sys
import cryptography
from cyphers.cbc import cbc
from cyphers.ecb import ecb

def main():
	if len(sys.argv[1:]) != 3:
		print("Usage: py main.py <ecb | cbc> <infile> <outfile>")
		return
	
	if sys.argv[1].lower() not in ['ecb', 'cbc']:
		print(f'You chose to incrypt using "{sys.argv[1]}" but the only valid modes are ecb or cbc.')
		return

	mode = sys.argv[1].lower()
	infile = sys.argv[2]
	outfile = sys.argv[3]

	if mode == 'ecb':
		ecb(infile, outfile)
	if mode == 'cbc':
		cbc(infile, outfile)


if __name__ == '__main__':
	main()