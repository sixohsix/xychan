xychan
======

xychan is a "chan-style" message board system like Wakaba, Kareha,
Futaba, etc. Unlike these systems it's written in Python instead of a
mess of Perl or PHP.

[Actions speak louder than words. You can try it out here.](http://xychan-beta.mike.verdone.ca/)


What is this, really?
---------------------

A "chan board" is a message board that allows for Anonymous
posting. Users can post messages without registering for an account or
even entering a name. However, there are means for them to
authenticate themselves and "prove" their identify if they so desire.

Another focus is the ability of users to post images. One image can be
included with every post. A thumbnail of the image appears with the
post.


Design Goals
------------

xychan is designed to be:

 * easily deployed on almosy any web server (via CGI, FastCGI, Passenger, or any WSGI runner)
 * easily configured (uses SQLAlchemy to work with any database, from
   SQLite3 to MySQL, PostgreSQL, etc.)
 * easily extended and customized with CSS or template modification
 * scalable (at least compared to those other message boards)
 * small yet powerful


Status
------

This is BETA quality software. It is not yet stable. It changes a lot.


Downloads
---------

 * The latest stable version is v0.3
 * The latest stable version in an easily deployable zip file: [here](http://mike.verdone.ca/xychan/xychan.zip)
 * The easiest way to get xychan if you are a Python pro:

       $ pip install xychan

 * Stable source packages are in the [GitHub files section](http://github.com/sixohsix/xychan/downloads)
 * Bleeding edge source for developers is in the [GitHub repository](http://github.com/sixohsix/xychan)
     * or in the backup repo at [mike.verdone.ca](http://mike.verdone.ca/git/xychan) ([browseable with gitweb](http://mike.verdone.ca/git/?p=xychan;a=summary))


How do I run it? - the EASY way (cgi)
-------------------------------------

 * Your web server needs Python 2.5 or higher
 * Your web server needs ImageMagick to support images on the board
 * Download the easily deployable zip file, above
 * Copy it to your webserver in an empty directory that supports CGI
 * Unzip it
 * Modify xychan.cgi in case there's anything you want to change there
 * Modify htaccess and copy it to .htaccess
 * Access path/to/xychan.cgi/setup on your webserver


How do I run it? - the SMART way
--------------------------------

 * Your web server needs Python 2.5 or higher
 * Your web server needs ImageMagick to support images in the board
 * Your web server needs the following Python packages installed:
   * bottle
   * sqlalchemy
   * Some kind of database (eg. sqlite3)
 * Untar the xychan codebase
 * In your WSGI server:: 

        from xychan import app
        app.configure_db("postgres://user:password@host/dbname")
        # (or some similar SQLAlchemy db url)
        app.configure_image_dir("/some/safe/path/in/your/filesystem")


License
-------

xychan is Free Software available under the GPL3 (GNU General Public
License v3).

Those wanting to make closed-source commercial forks should contact me.


Why is it called xychan?
------------------------

Characters typed at random.
