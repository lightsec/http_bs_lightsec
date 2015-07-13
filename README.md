Sample Base Station using liblightsec
=====================================

HTTP-based implementation for a sample Base Station which uses liblightsec.


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
   
    ```cd src/httplightsec; python run.py```

2. Go to _/admin_ and create a sample user and a sample sensor associated to it.

3. Go to _/sensors/{sample-mac}_ and as you are not logged in, you will be redirected to the login page.

4. Introduce the username and password of the sample user created before.

5. Then, you will be reditected to _/sensors/{sample-mac}_ and you will see the information from [liblightsec's fourth step](https://github.com/lightsec/liblightsec).
