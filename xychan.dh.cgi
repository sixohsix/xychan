#!/home/iamstupid/py27/bin/python -O

# CGI config for dreamhost. Sorta working.

import xychan

from xychan import app

app.configure_db("sqlite:////home/iamstupid/test.db")
app.configure_image_dir("/home/iamstupid/_images")

from wsgiref.handlers import CGIHandler
CGIHandler().run(app)
