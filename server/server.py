#!/usr/bin/python3

from flask import Flask, request, abort, render_template
from backend import OTP_Backend

app = Flask(__name__)
backend = OTP_Backend()

def render_page():
    return render_template("index.html",
            psk=backend.psk, 
            cntr=backend.cntr,
            success=backend.verified
            )


# Frontent Request Handling
@app.route("/")
def show_index():
    return render_page()
    
@app.route("/generate_keys")
def generate_keys():
    backend.generate_keys()
    return render_page()

@app.route("/verify_key")
def verify_key():
    if not 'token' in request.args:
        abort(400)

    token = request.args['token']
    backend.verify_key(token)
    return render_page()

if __name__ == "__main__":
    app.run(port=8181)

