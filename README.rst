========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis|
        | |coveralls| |codecov|
        | |codacy|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/zfit-interface/badge/?style=flat
    :target: https://readthedocs.org/projects/zfit-interface
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.org/zfit/zfit-interface.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/zfit/zfit-interface

.. |coveralls| image:: https://coveralls.io/repos/zfit/zfit-interface/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/zfit/zfit-interface

.. |codecov| image:: https://codecov.io/github/zfit/zfit-interface/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/zfit/zfit-interface

.. |codacy| image:: https://img.shields.io/codacy/grade/[Get ID from https://app.codacy.com/app/zfit/zfit-interface/settings].svg
    :target: https://www.codacy.com/app/zfit/zfit-interface
    :alt: Codacy Code Quality Status

.. |version| image:: https://img.shields.io/pypi/v/zfit-interface.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/zfit-interface

.. |wheel| image:: https://img.shields.io/pypi/wheel/zfit-interface.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/zfit-interface

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/zfit-interface.svg
    :alt: Supported versions
    :target: https://pypi.org/project/zfit-interface

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/zfit-interface.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/zfit-interface

.. |commits-since| image:: https://img.shields.io/github/commits-since/zfit/zfit-interface/v0.0.1.svg
    :alt: Commits since latest release
    :target: https://github.com/zfit/zfit-interface/compare/v0.0.1...master



.. end-badges

zfit model fitting interface for HEP

* Free software: BSD 3-Clause License

Installation
============

::

    pip install zfit-interface

You can also install the in-development version with::

    pip install https://github.com/zfit/zfit-interface/archive/master.zip


Documentation
=============


https://zfit-interface.readthedocs.io/


Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
