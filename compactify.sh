#!/bin/sh

mkdir -p _compactify_build dist
rm -rf _compactify_build/*
rm -rf dist/*
cp -a xychan _compactify_build/
cp -a `python -c 'import sqlalchemy;print sqlalchemy.__path__[0]'` _compactify_build/
cp -a `python -c 'import bottle;print bottle.__file__[:-1]'` _compactify_build/
find _compactify_build | grep ~$ | xargs rm
find _compactify_build | grep \\.pyc$ | xargs rm
find _compactify_build | grep \\.pyo$ | xargs rm

cat > _compactify_build/__main__.py <<EOF

if __name__=='__main__':
    from xychan import app
    from wsgiref.handlers import CGIHandler
    CGIHandler().run(app)

EOF

python -OO -m compileall _compactify_build
find _compactify_build | grep \\.py$ | xargs rm
cd _compactify_build
zip ../dist/xychan.zip -r *
cd -
cat - > dist/xychan.cgi <<EOF
#!/usr/bin/python -O

import sys
import os
sys.path.insert(0, sys.path[0] + os.sep + 'xychan.zip')
import xychan
from xychan import app
from wsgiref.handlers import CGIHandler
CGIHandler().run(app)
EOF

chmod +x dist/xychan.cgi
