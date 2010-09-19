xychan
======

xychan is a "chan-style" message board system like Wakaba, Kareha,
Futaba, etc. Unlike these systems it's written in Python instead of a
mess of Perl or PHP.


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


License
-------

xychan is Free Software available under the GPL (GNU General Public
License).

Those wanting to make closed-source commercial forks can contact me
for licensing rates.


Why is it called xychan?
------------------------

Characters typed at random.
