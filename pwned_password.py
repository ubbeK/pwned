"""
Prerequisite:
    Install Python 3.X from https://www.python.org/downloads/release

Usage:
    python .\pwned_password.py SomePlainPassword
"""

import hashlib
import requests
import sys

if len(sys.argv) < 2:
    print("Please supply your password as the first argument.")
    sys.exit()

plain_pw = sys.argv[1]
hash_object = hashlib.sha1(str.encode(plain_pw))
hex_dig = hash_object.hexdigest()

response = requests.get("https://api.pwnedpasswords.com/range/{0}".format(hex_dig[0:5]))

if str(hex_dig[5::].upper()) in str(response.text):
    print("Your password has been pwned by some 1337 HaXXor.")
else:
    print("OK: Password is fine.")