[![Stories in Ready](https://badge.waffle.io/drvinceknight/ghtalks.svg?label=ready&title=Ready)](http://waffle.io/drvinceknight/ghtalks)
[![Build Status](https://travis-ci.org/drvinceknight/ghtalks.svg?branch=master)](https://travis-ci.org/drvinceknight/ghtalks)
[![Stories in Ready](https://badge.waffle.io/drvinceknight/ghtalks.svg?label=ready&title=Ready)](http://waffle.io/drvinceknight/ghtalks)

# gh-talks

Share and organise your slides easily.

Quickly build an `index.html` file of all talks in a directory.
This is designed to work with [gh-pages](https://pages.github.com/) so that you
can easily keep your slides in one place and make them available to all.

# Installation

The simplest approach is to run:

    pip install ghtalks

You can also:

    git clone https://github.com/drvinceknight/ghtalks.git
    cd gh-talks
    python setup.py install

# Usage

In any given directory each talk must live in a directory with the following
naming convention: `date-title` where `date` must follow the [iso
convention](https://xkcd.com/1179/).

Here are some examples:

    2015-12-15-my-christmas-day-talk
    2000-01-01-y2k-is-here

Note the use of `dashes` for the name.

In that directory you can have whatever other files you want but there are two
files that are relevant to the package:

1. `index.html` (or `index.pdf`): the actual slides
2. `urls.yml`: a yml file containing a list of urls that you want to appear on
   the `index.html` (**you do not need to have this file in the directory).

Note that `gh-talks` will recursivelly search through the current directory so
your talk directories can be organised how you wish.

Here is an exammple of a valid file structure:

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


Note that you can include a `header.html` and `head.html` file with links to
css.
For example to create the site visible [here](vincent-knight.com/gh-talks) the
following was used:

    gh-talks -hd examples/head.html -hr examples/header.html -fr
    examples/footer.html -s

This is meant to work seamlously with a [jekyll](http://jekyllrb.com/) site deployed with [gh-pages](https://pages.github.com/).

# Contributing

Please do raise issues and pull requests: anything is welcome.
