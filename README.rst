quarto_gcc_kernel
==================

This is a fork of the gcc_kernel from the Jupyter project. 
It is intended to be used as a simple example of a Jupyter kernel that can take advantage of the specific ways in which Quarto communicates additional information during execution.

Below, you will find the original README from the `gcc_kernel <https://github.com/jupyter/gcc_kernel/>`_ project.

gcc_kernel
-----------

``gcc_kernel`` is a simple example of a Jupyter kernel. This repository
complements the documentation on wrapper kernels here:

http://jupyter-client.readthedocs.io/en/latest/wrapperkernels.html

Installation
------------

From PyPI
~~~~~~~~~

To install ``gcc_kernel`` from PyPI::

    pip install gcc_kernel
    
From Git using Conda
~~~~~~~~~~~~~~~~~~~~

To install ``gcc_kernel`` from git into a Conda environment::

    git clone https://github.com/jupyter/gcc_kernel
    cd gcc_kernel
    conda create -n ker jupyter
    conda activate ker
    pip install .


Using the Gcc kernel
---------------------
**Notebook**: The *New* menu in the notebook should show an option for an Gcc notebook.

**Console frontends**: To use it with the console frontends, add ``--kernel gcc`` to
their command line arguments.
