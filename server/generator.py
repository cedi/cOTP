#/usr/bin/python3

import hashlib
import binascii
from generate_token import generate_token

class OTP_Generator:
    def __init__(self, psk, cntr):
        self.psk = psk
        self.cntr = cntr

    def generate(self):
        if self.cntr <= 0:
            raise Exception("Counter is null")
       
        token = generate_token(self.cntr, self.psk)
       
        self.cntr = self.cntr -1
        return token

