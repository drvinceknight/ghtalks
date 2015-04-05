.. gh-talks documentation master file, created by
   sphinx-quickstart on Sun Apr  5 17:15:54 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to gh-talks's documentation!
====================================

The idea behind this python package is that it allows you to quickly index all
your slides.

Installation
------------

To install simply::

    pip install ghtalks


Basic usage
-----------

After installing, assume you have a directory that looks something like this::

    Talks
    ├── talks
    │   └── 2015-04-05-using-gh-talks
    │       └── index.html
    │   └── Archive
    │       └── 2000-01-01-y2k-is-here
    │           └── index.html
    │           └── .html
    │       └── 2012-12-15-my-christmas-day-talk
    │           └── index.tex
    │           └── index.pdf
    │           └── images
    └── README.md
    └── header.html
    └── head.html
    └── footer.html
    └── main.css

Where :code:`2015-04-05-using-gh-talks` and
:code:`2012-12-15-my-christmas-day-talk` are directories that contain talks.
The :code:`head.html`, :code:`header.html` and :code:`footer.html` files can be
considered to be template files.

To generate an `index.html` file that will find the directories formatted as
above (with an `ISO formatted <https://xkcd.com/1179/>`_ date at the top of the name)
you can simply run::

    gh-talks -s

Take a look at the `github <https://github.com/drvinceknight/ghtalks>`_ repository where there is an :code:`examples` directory that was used to create `this site <http://vincent-knight.com/ghtalks/>`_

You do not need to keep the :code:`head.html`, :code:`header.html` and :code:`footer.html` files in the same directory as you want the :code:`index.html` file.
There are command line arguments that you can fun to point at particular files::

    gh-talks -s -hd path-to-head.html -hr path-to-header.html -fr path-to-footer.html


Contributing
------------

Any contributions are more than welcome.

A test suite is in place, here is the status on travis:

.. image:: https://travis-ci.org/drvinceknight/ghtalks.svg?branch=master
    :target: https://travis-ci.org/drvinceknight/ghtalks

There is also a waffle board for issues here:

.. image:: https://badge.waffle.io/drvinceknight/ghtalks.svg?label=ready&title=Ready
   :target: https://waffle.io/drvinceknight/ghtalks
   :alt: 'Stories in Ready'

Please get in touch!

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

