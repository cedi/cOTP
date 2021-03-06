#/usr/bin/python3

import hashlib
import binascii
from generate_token import generate_token

class OTP_Verifyer:
    def __init__(self, psk, cntr):
        self.psk = psk
        self.cntr = cntr
        self.treshold = 5

    def verify(self, otp_token):
        possible_tokens = dict()

        for i in range(self.cntr-self.treshold, self.cntr+1):
            possible_tokens[generate_token(i, self.psk)] = i
       
        updated_cntr = self.cntr

        if otp_token in possible_tokens:
            updated_cntr = possible_tokens[otp_token]
            print("Used/Expected {}/{}".format(updated_cntr, self.cntr))
            self.cntr = updated_cntr -1
            
            return 200
        
        return 403
      
