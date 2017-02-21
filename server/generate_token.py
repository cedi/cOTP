#/usr/bin/python3

import hashlib
import binascii

def _simplify_token(token):
    token_cntr = 0
    char_cntr = 0
    shortened_token = ""
    while token_cntr < 6 and char_cntr < len(token):
        char = token[char_cntr]

        if char.isdigit():
            shortened_token += char
            token_cntr += 1

        char_cntr += 1    

    return shortened_token 


def generate_token(cntr, psk):
    token = str(psk)
    
    for i in range(cntr):
        token = hashlib.sha256(token.encode()).hexdigest()
    
    return _simplify_token(token)
