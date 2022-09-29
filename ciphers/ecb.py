import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from ciphers.constants import *

def ecb(infile: str, outfile: str):
	print("ecb")
	key = os.urandom(CHUNKSIZE)
	iv = os.urandom(CHUNKSIZE)
	cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
	encryptor = cipher.encryptor()

	_encrypt_file(infile, outfile, encryptor)

	return

def _encrypt_file(infile: str, outfile: str, encryptor: Cipher):

	f = open(infile, 'rb')
	header = f.read(BMPHEADER)
	enc_out = b''

	while True:

		data = f.read(CHUNKSIZE)
		if not data:
			break

		enc_out += encryptor.update(data)

	with open(f'outputs/{outfile}', 'wb') as f2:
		f2.write(header)
		f2.write(enc_out)

