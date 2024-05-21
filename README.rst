quarto_gcc_kernel
==================

This is a fork of the
`quarto_echo_kernel <https://github.com/quarto-dev/quarto_echo_kernel>`_
project. It is a simple example of a Jupyter kernel that runs the GNU Compiler
Collection (GCC) to compile and run C code.

Installation
------------

From PyPI
~~~~~~~~~

To install ``gcc_kernel`` from PyPI::

    pip install gcc_kernel
    
From Git using Conda
~~~~~~~~~~~~~~~~~~~~

To install ``gcc_kernel`` from git::

    git clone https://github.com/jupyter/gcc_kernel
    cd gcc_kernel
    pip install .


Using the Gcc kernel
---------------------
**Notebook**: The *New* menu in the notebook should show an option for an Gcc notebook.

**Console frontends**: To use it with the console frontends, add ``--kernel gcc`` to
their command line arguments.

Configuration
-------------

Currently, the kernel can't be configured and will always use:

- ``-std=c99`` for C code
- Wrap the code in a ``main`` function if it doesn't already have one with:

  ```c
  #include <assert.h>
  #include <stdbool.h>
  #include <stddef.h>
  #include <stdint.h>
  #include <stdio.h>
  #include <stdlib.h>
  ```

Contributing
------------

I use this project for my courses and just fit my needs. If you want to improve
it to fit yours, your contributions are welcome:)