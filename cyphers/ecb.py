import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def ecb(infile: str, outfile: str):
	print("ecb")
	key = os.urandom(16)
	iv = os.urandom(16)
	cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
	encryptor = cipher.encryptor()

	# enc = encryptor.update() + encryptor.finalize()

	with open(infile, 'rb') as f:

		enc = encryptor.update(f.read(16)) + encryptor.finalize()

		with open(f'outputs/{outfile}', 'wb') as f2:
			f2.write(enc)


	return
