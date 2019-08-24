activate_this='/var/www/Hogwarts/env/bin/activate_this.py'
with open(activate_this) as f:
	code=compile(f.read(), activate_this, 'exec')
	exec(code, dict(__file__=activate_this))

import os, sys, logging

sys.path.insert(0, '/var/www/Hogwarts/src')
from hogwarts import app as application
