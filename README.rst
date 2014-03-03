#######
gengzip
#######

.. image:: https://travis-ci.org/leetreveil/gengzip.png
        :target: https://travis-ci.org/leetreveil/gengzip

Python generators are cool. The compress() function returns a python generator with the gzipped data.


Installation
-----------------

Install via `pip`_:

.. code:: bash

    $ pip install gengzip


Usage
-----

.. code:: python

    input = ['123', '45']
    # compress() returns a python generator object
    # compresslevel defaults to 6
    for compressed in gengzip.compress(input, compresslevel=6):
        print compressed


gzip data and write to file:

.. code:: python

    input = ['123', '45']
    with open('output.gz', 'w') as f:
        for compressed in gengzip.compress(input):
            f.write(compressed)

Licence
-----------------
MIT

.. _pip: http://www.pip-installer.org/