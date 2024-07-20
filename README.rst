quarto_gcc_kernelf
==================

**This kernel has been abandoned in favor of [`jupygcc`](https://github.com/benabel/jupygcc) magic.**

This is a fork of the
`quarto_echo_kernel <https://github.com/quarto-dev/quarto_echo_kernel>`_
project. It is a simple example of a Jupyter kernel that runs the GNU Compiler
Collection (GCC) to compile and run C code.

Installation
------------

Not published to Pypi, you can install it from github:
    
    pip install https://github.com/benabel/quarto_gcc_kernel/archive/main.zip

You can verify the installation with:

    jupyter kernelspec list


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

Cell metadata
-------------

Currently, the only cell metadata handled is `stdin` for non-interactive `scanf` calls:

```{c}
//| stdin: 10
int n;
printf("How many lines? ");
scanf("%d", &n);
printf("\n%d lines\n");
```

Contributing
------------

I use this project for my courses and just fit my needs. If you want to improve
it to fit yours, your contributions are welcome:)