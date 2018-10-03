========
langevin
========


.. image:: https://img.shields.io/pypi/v/langevin.svg
        :target: https://pypi.python.org/pypi/langevin

.. image:: https://img.shields.io/travis/floompytuesday/langevin.svg
        :target: https://travis-ci.org/floompytuesday/langevin

.. image:: https://readthedocs.org/projects/langevin/badge/?version=latest
        :target: https://langevin.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/floompytuesday/langevin/shield.svg
     :target: https://pyup.io/repos/github/floompytuesday/langevin/
     :alt: Updates
.. image:: https://coveralls.io/repos/github/floompytuesday/langevin/badge.svg?branch=master
:target: https://coveralls.io/github/floompytuesday/langevin?branch=master



This is a one-dimensional Langevin Dynamics program written in Python.  It can be run by typing "python langevin.py" in the appropriate directory.
Variables such as intial position, initial velocity, and total time can be entered in the command line by using flags (--initial_positon=10) after langevin.py
Default values for these variables can be found in the source code.  Output will be written to a .txt file with index, time, position, and velocity.
A histogram (histogram.png) will be created with the times of 100 runs that ended with the particle hitting the far wall.  There will also be a plot of trajectory (trajectory.png) of the
last of the 100 runs that hit the far wall.


* Free software: MIT license
* Documentation: https://langevin.readthedocs.io.


Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
