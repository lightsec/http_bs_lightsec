pyNist800-108
=============

Python implementation of Nist SP 800-108 KDF in Counter Mode


Installation
------------

Why would you want to install it?

    pip install git+https://github.com/lightsec/http_bs_lightsec.git


Requirements
------------

The required packages are automatically installed in the procedure described above.

However, if you are going to contribute to this project, you might want to install __only__ the project's dependencies in your [virtualenv](http://virtualenv.readthedocs.org).

You can install them using the _requirements.txt_ file in the following way:

        pip install -r requirements.txt

Usage
-----

1. Run the web server.
```
python webapp.py
```
2. Go to _/admin_ and create sample user.
3. Go to _/settings_ and as you are not logged in, you will be redirected to the login page.
4. Introduce the username and password created before.
5. Then, you will be reditected to _settings_ and you will be able to see a message.