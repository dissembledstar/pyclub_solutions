#!/usr/bin/env python

# we assume python 2.7


import requests
import json
import base64
import re # now we have 2 problems

resp = requests.get('http://thepythonclub.org:8083/challenge3')

# grab the username we need
target_user = resp.text.split('"')[1]
user_id= ""
passwd= ""

print "Going after: " + target_user

# grab the links
urls = re.findall('http.*?txt',resp.text)

# grab our userid file
user_file = urls[0]

resp = requests.get(user_file)

# split out our lines
data = resp.content.split('\n')

# find our user
for line in data:
	if target_user in line :
	# grab the userid
		user_id = line.split('"')[1]
		print "Cool, found userid: " + user_id
		break	

# grab our passwd file
passwd_file = urls[1]

resp = requests.get(passwd_file)

# split out our lines
data = resp.content.split('\n')

# find our password
for line in data:
	if user_id in line :
	# grab the password
		enc_passwd = line.split(':')[1]
		passwd = base64.b64decode(enc_passwd)
		print "Sick, found password:" + passwd 
		break

# hooray!
solution = passwd

# send the answer
print
print "Sending solution: " + str(solution)
payload = {'answer' : solution }
print json.dumps(payload)
resp = requests.post('http://thepythonclub.org:8083/challenge3', data=json.dumps(payload))
print resp.text
