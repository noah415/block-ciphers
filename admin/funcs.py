import urllib.parse
import os, sys
from Crypto.Util.Padding import pad, unpad
from ciphers.cbc import _decrypt, _encrypt
from ciphers.constants import CHUNKSIZE
from base64 import b64encode, b64decode

def submit(msg: str, cipher):
  msg = _encrypt(msg, cipher).decode('utf-8')
  print(f'This is your encrypted message: {msg[CHUNKSIZE:]}')
  response = input('\nWould you like to try to hack into the admin system (y/n)? > ').lower()

  # for 'hacking' into the admin system
  if response == 'y':
    msg = hack(msg)
    print(f'\nThis is your tampered data\niv: {msg[:CHUNKSIZE]}\nmessage: {msg[CHUNKSIZE:]}\n')
  
  return msg

def verify(msg, key):
  plaintext = _decrypt(msg, key)
  print(f'This is your decrypted message: {plaintext}')
  if b';admin=true;' in plaintext:
    print(f'\nVerification: true\n\n--- WELCOME TO THE SYSTEM ADMIN ---\n')
  else:
    print(f'\nVerification: false\n\n--- WELCOME TO THE SYSTEM USER ---\n')

def hack(data):
  # to hack the system, you must input: 1111119admin9true9
  pos1 = 32
  pos2 = 38
  pos3 = 43
  print('\nHacking into the admin system now...')
  raw = b64decode(data)
  list1 = list(raw)
  list1[pos1] = list1[pos1]^2
  list1[pos2] = list1[pos2]^4
  list1[pos3] = list1[pos3]^2
  raw = bytes(list1)
  return b64encode(raw)
