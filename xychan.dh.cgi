#!/home/iamstupid/py27/bin/python -O

# CGI config for dreamhost. Sorta working.

import sys
import os
#sys.path.insert(0, sys.path[0] + os.sep + 'xychan.zip')
import xychan
from xychan import app
from xychan.db import configure_db
from xychan.image_store import configure_image_dir

configure_db("sqlite:////home/iamstupid/test.db")
configure_image_dir("/home/iamstupid/_images")
from wsgiref.handlers import CGIHandler
CGIHandler().run(app)
