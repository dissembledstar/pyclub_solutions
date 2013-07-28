#!/usr/bin/env python

# we assume python 2.7

import requests
import json

# incomplete list, good enough to solve at least once
wordlist = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen']

resp = requests.get('http://thepythonclub.org:8082/challenge2')

#print "DBG: |" + resp.text + "|"

# grab the formula text
problem = resp.text.split('"')[1]

problem = problem.split()

# problem is now a list
# remove the last two elements
problem = problem [:-2]

#print "DBG: |" + str(problem) + "|"

formula = ""
for word in problem :
	word = word.strip()
	try: 
		formula += str(wordlist.index(word))
	except:
		# probably an operator
		if word in "minus":
			formula += '-'
		if word in "plus":
			formula += '+'
	
solution = eval(formula)

# convert solution back to word
solution = wordlist[solution]

# send the answer
print "Sending solution: " + str(solution)
payload = {'answer' : solution }
resp = requests.post('http://thepythonclub.org:8082/challenge2', data=json.dumps(payload))
print resp.text
