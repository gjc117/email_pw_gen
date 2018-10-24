import os
import random
import string
import json
from random import randint

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(2048))

names = json.loads(open('names.json').read())
domain = json.loads(open('emailDomains.json').read())

for name in names:
	num_rand = ''.join(random.choice(string.digits))
	domain_rand = ''.join(domain[randint(0,99)])
	email = name.lower() + num_rand + '@'+ domain_rand
	password = ''.join(random.choice(chars) for i in range(12))

	print(f'{email} \t\t {password}')
