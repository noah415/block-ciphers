import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from ciphers.constants import *

def ecb(infile: str, outfile: str):
	
	print(f'Encrypting {infile} using ECB ...')
	key = os.urandom(CHUNKSIZE)

	cipher = Cipher(algorithms.AES(key), modes.ECB())
	encryptor = cipher.encryptor()

	_encrypt_file(infile, outfile, encryptor)
	print(f'\nEcryption done - outputs/{outfile}')

	return

def _encrypt_file(infile: str, outfile: str, encryptor: Cipher):

	f = open(infile, 'rb')
	header = f.read(BMPHEADER)
	enc_out = b''

	while True:

		data = f.read(CHUNKSIZE)
		if not data:
			break

		len_diff = CHUNKSIZE - len(data)
		data += b'\0' * len_diff

		enc_out += encryptor.update(data)

	with open(f'outputs/{outfile}', 'wb') as f2:
		f2.write(header)
		f2.write(enc_out)

