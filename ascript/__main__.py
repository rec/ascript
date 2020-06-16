"""
🎦 Script asciinema movies 🎦
====================================================================


USAGE
-------

.. code-block:: bash

    ascript my_file.py [README.rst]

"""

import sys

__all__ = ('main',)


def main(source, target=None):
    """Print documentation for a file or module

    ARGUMENTS
      path
        path to the Python file or module.

      target
        path to the output file or ``None``, in which case
        output is printed to stdout
    """
    lines = []

    if target:
        with open(target, 'w') as fp:
            print(lines, file=fp)
    else:
        print(lines)


if __name__ == '__main__':
    main(*sys.argv[1:])
