# -*- coding: utf-8 -*-
"""
Created on Tue Oct 03 20:21:17 2017

@author: Celin
"""


import os,sys
from flask import Flask,request
from apiai import ApiAI

CLIENT_ACCESS_TOKEN = 'your_client_access_token_from_api_ai'
PAGE_ACCESS_TOKEN = 'hello'
VERIFY_TOKEN = 'hellos'



app = Flask(__name__)
@app.route('/',methods=['GET'])
def handle_verification():
    if (request.args.get('hub.verify_token', '') == VERIFY_TOKEN):
        print("Verified")
        return request.args.get('hub.challenge', '')
    else:
        print("Wrong token")
        return "Error, wrong validation token"
    
if __name__ =="__main__":
    app.run(debug=True,port = 80)



@app.route('/',methods=['POST'])
def receive_message():
    data_rec = request.get_json()    
    if data_rec["object"] == "page":
        for entry in data_rec["entry"]:
            for messg_event in entry["messaging"]:
                if messg_event.get("message"):
                    
                    sender_id = mssg_event["sender"]["id"]
                    recipient_id = mssg_event["recipient"]["id"]
                    
    