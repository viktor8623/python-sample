python-sample
=============

Simple python example for UI testing based on data-driven approach.
It allows performing tests with a different set of data without changing the test script.
To create test just fill out data in the table in python_sample/data/search_queries.xlsx


System requirements
-------------------

1. Python 3.7.3
2. Hatch 0.20.0
3. Webdriver for google chrome



Installation
------------

code-block::

    $ pip3 install --user hatch

    $ git clone https://github.com/viktor8623/python-sample.git

    $ cd python-sample

    $ hatch test -ta "--url=https://shop.by/"



**Note! Tests fail.**