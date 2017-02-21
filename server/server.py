#!/usr/bin/python3

import traceback
import random

from flask import Flask, request, abort, render_template
from generator import OTP_Generator
from verifyer import OTP_Verifyer

app = Flask(__name__)

class OTP_Backend:
    def __init__(self):
        self.psk=""
        self.cntr=""
        self.verified=403
        self.token=""
        self.generator = ""
        self.verifyer = ""

    def verify(self, token):
        self.verified = self.verifyer.verify(token)

    def tokenize(self):
        self.token = self.generator.generate()

    def generate_keys(self):        
        self.psk = int(random.random() * 100000000)
        self.cntr = int(random.random() * 1000)
        self.generator = OTP_Generator(self.psk, self.cntr)
        self.verifyer = OTP_Verifyer(self.psk, self.cntr)


backend = OTP_Backend()

generated_token = ""

def render_page():
    return render_template("index.html",
            psk=backend.psk, 
            cntr=backend.cntr,
            success=backend.verified,
            token=backend.token
            )

# Frontent Request Handling
@app.route("/")
def show_index():
    return render_page()

@app.route("/generate_keys")
def generate_keys():
    backend.generate_keys()
    return render_page()


@app.route("/generate_token")
def generate_token():
    backend.tokenize()
    return render_page()

@app.route("/verify_key")
def verify_key():
    if not 'token' in request.args:
        abort(400)
    
    token = request.args['token']

    backend.verify(token)
    return render_page()

if __name__ == "__main__":
    app.run(port=8181)

