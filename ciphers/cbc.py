import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from ciphers.constants import *

def cbc(infile: str, outfile: str):

	print(f'Encrypting {infile} using CBC ...')

	key = os.urandom(CHUNKSIZE)
	iv = os.urandom(CHUNKSIZE)

	cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
	encryptor = cipher.encryptor()

	_encrypt_file(infile, outfile, encryptor)

	print(f'\nEcryption done - outputs/{outfile}')

	return

def _encrypt_file(infile: str, outfile: str, encryptor: Cipher):

	f = open(infile, 'rb')

	bmp = False
	if '.bmp' == infile[-4:] and '.bmp' == outfile[-4:]:
		bmp = True
		header = f.read(BMPHEADER)

	enc_out = b''

	while True:

		data = f.read(CHUNKSIZE)
		if not data:
			break

		len_diff = CHUNKSIZE - len(data)
		data += bytes(hex(len_diff), 'utf-8') * len_diff

		iv = encryptor.update(data)
		enc_out += iv

	with open(f'outputs/{outfile}', 'wb') as f2:

		if bmp:
			f2.write(header)

		f2.write(enc_out)