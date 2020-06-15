====================
pymt_prms_streamflow
====================


.. image:: https://img.shields.io/badge/CSDMS-Basic%20Model%20Interface-green.svg
        :target: https://bmi.readthedocs.io/
        :alt: Basic Model Interface

.. image:: https://img.shields.io/badge/recipe-pymt_prms_streamflow-green.svg
        :target: https://anaconda.org/csdms-stack/pymt_prms_streamflow

.. image:: https://img.shields.io/travis/pymt-lab/pymt_prms_streamflow.svg
        :target: https://travis-ci.org/pymt-lab/pymt_prms_streamflow

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
        :target: https://github.com/csdms/pymt
        :alt: Code style: black


PyMT plugin for the PRMS6 Streamflow component


* Free software: MIT license
* Documentation: https://www.usgs.gov/software/precipitation-runoff-modeling-system-prms




============== ========================================
Component      PyMT
============== ========================================
PRMSStreamflow `from pymt.models import PRMSStreamflow`
============== ========================================

---------------
Installing pymt
---------------

Installing `pymt` from the `conda-forge` channel can be achieved by adding
`conda-forge` to your channels with:

.. code::

  conda config --add channels conda-forge

*Note*: Before installing `pymt`, you may want to create a separate environment
into which to install it. This can be done with,

.. code::

  conda create -n pymt python=3
  source activate pymt

Once the `conda-forge` channel has been enabled, `pymt` can be installed with:

.. code::

  conda install pymt

It is possible to list all of the versions of `pymt` available on your platform with:

.. code::

  conda search pymt --channel conda-forge

-------------------------------
Installing pymt_prms_streamflow
-------------------------------

Once `pymt` is installed, the dependencies of `pymt_prms_streamflow` can
be installed. Start by appending `csdms-stack` to your channels with:

.. code::

  conda config --append channels csdms-stack

then install the dependencies with:

.. code::

  conda install bmi-fortran=2.0 prms prms_streamflow

To install `pymt_prms_streamflow`,

.. code::

  conda install pymt_prms_streamflow
