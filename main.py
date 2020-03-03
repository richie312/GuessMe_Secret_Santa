# -*- coding: utf-8 -*-
import flask
from flask import Flask, request, jsonify,redirect
from flask import render_template
from datetime import datetime    
from mail import *


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def home():
    letter_list = ["A","B","C","D","E","F","G","H","I","J",
                   "K","L","M","N","O","P","Q","R","S","T","U","V",
                   "W","X","Y","Z"]
    
    name = "Aritra Chatterjee"
    reverse_name = name.split(" ")[::-1]
    text = ('').join(reverse_name).upper()
    """ Shift by 4 letters"""
    cipher_name = []
    for i in range(len(text)):
        cipher_name.append(letter_list[letter_list.index(text[i])+4])
    display_name = ('').join(cipher_name)
    return render_template('home.html',display_name = display_name)

@app.route('/parse_data', methods=['POST'])
def parse_data():
    rtext = request.form
    if rtext['text'] == 'Aritra Chatterjee':
        mailto('aritra@capitalnumbers.com')
        template = "Thank You.html"
    else: 
        template = "Try Again.html"         
    return render_template(template)

if __name__ == '__main__':
    app.run(host = '0.0.0.0',port = 5000,debug = True)

