#!/usr/bin/env python

# we assume python 2.7

import requests
import json
import base64
import re # now we have 2 problems

resp = requests.get('http://thepythonclub.org:8083/challenge3')

# grab the username we need
target_user = resp.text.split('"')[1]
target_userid = ""
passwd = ""
solution = ""

print "Going after: " + target_user

# grab the links
urls = re.findall('http.*?json',resp.text)

# grab our userid file
user_file = urls[0]

resp = requests.get(user_file)

# find our user
data = json.loads (resp.content)
for userid, info_dict in data.items():
	if info_dict [ 'Name' ]  == target_user :
		target_userid = userid
		print "Cool, found userid: " + target_userid

# grab our passwd file
passwd_file = urls[1]

resp = requests.get(passwd_file)

# find our password
data = json.loads (resp.content)

for userid, password in data.iteritems():
	if userid == target_userid :
		solution = base64.b64decode(password)
		print "Sick, found password:" + solution 
		break

# send the answer
payload = {'answer' : solution }
resp = requests.post('http://thepythonclub.org:8083/challenge3', data=json.dumps(payload))
print resp.text
