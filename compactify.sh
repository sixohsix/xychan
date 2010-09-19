#!/bin/sh

# This script creates the xychan.zip file.

mkdir -p _compactify_build dist
rm -rf _compactify_build/*
rm -rf dist/*
cp -a xychan _compactify_build/
cp -a `python -c 'import sqlalchemy;print sqlalchemy.__path__[0]'` _compactify_build/
cp -a `python -c 'import bottle;print bottle.__file__[:-1]'` _compactify_build/
find _compactify_build | grep ~$ | xargs rm
find _compactify_build | grep \\.pyc$ | xargs rm
find _compactify_build | grep \\.pyo$ | xargs rm

python -OO -m compileall _compactify_build
find _compactify_build | grep \\.py$ | xargs rm
cp xychan.cgi _compactify_build/
cp htaccess _compactify_build/htaccess
chmod +x _compactify_build/xychan.cgi
mkdir -p _compactify_build/_images/thumbs
cd _compactify_build
zip ../dist/xychan.zip -r *
cd -
