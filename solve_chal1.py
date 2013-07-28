#!/usr/bin/env python

# we assume python 2.7

import requests
import base64 
import json 
resp = requests.get('http://thepythonclub.org:8081/challenge1')

#print "DBG: |" + resp.text + "|"

# grab the base64 text
enc_text = resp.text.split()[-1]

# strip out quotes
enc_text = enc_text.replace( '\"' , '' )

dec_text = base64.b64decode (enc_text)
#print enc_text
#print dec_text

# send the answer
payload = {'answer' : dec_text }
resp = requests.post('http://thepythonclub.org:8081/challenge1', data=json.dumps(payload))
print resp.text
