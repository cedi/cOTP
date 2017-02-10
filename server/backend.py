#/usr/bin/python3

import hashlib
import binascii

class OTP_Backend:

    def __init__(self):
        self.psk=""
        self.cntr=""
        self.verified=False

    def verify_key(self, token):
        print("verify_key: token={}".format(token))
        if(token is ""):
            self.verified=False
        else:
            self.verified=True

    def generate_keys(self):
        self.psk=984
        self.cntr=5
        
