#!/usr/bin/env python3

# https://gist.github.com/ivanov17/67a8acb1bfd0e7b5e3929aa9fbc379a5

# Convert certbot private_key.json to Abstract Syntax Notation One (ASN.1)
# Usage: python3 jwk2asn1.py private_key.json > private_key.asn1
# openssl asn1parse -genconf private_key.asn1 -noout -out private_key.der
# openssl rsa -in private_key.der -inform der > private_key.pem
#
# Originally developed and published by Jon Lundy under the MIT License, 2015
# Updated to Python 3.6 by Anton Ivanov, Agorist International Conspiracy, 2020

from sys import argv
from json import load
from base64 import urlsafe_b64decode
from binascii import hexlify

with open(argv[1]) as fp:
    pkey = load(fp)

def enc(data):
    missing_padding = 4 - len(data) % 4
    if missing_padding:
        data += b'=' * missing_padding
    data = hexlify(urlsafe_b64decode(data))
    return '0x' + data.decode('utf_8').upper()

for k,v in tuple(pkey.items()):
    if k == 'kty': continue
    pkey[k] = enc(v.encode())

print("asn1=SEQUENCE:private_key\n[private_key]\nversion=INTEGER:0")
print("n=INTEGER:{}".format(pkey['n']))
print("e=INTEGER:{}".format(pkey['e']))
print("d=INTEGER:{}".format(pkey['d']))
print("p=INTEGER:{}".format(pkey['p']))
print("q=INTEGER:{}".format(pkey['q']))
print("dp=INTEGER:{}".format(pkey['dp']))
print("dq=INTEGER:{}".format(pkey['dq']))
print("qi=INTEGER:{}".format(pkey['qi']))
