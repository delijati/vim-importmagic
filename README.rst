vim-importmagic
===============

Vim plugin to import not imported modules using `importmagic <https://github.com/alecthomas/importmagic>`_


Usage
=====

To import not imported modules call ``:ImportMagic`` command. It will add
imports to the current python file.


Installation
============

We need to install `importmagic <https://github.com/alecthomas/importmagic>`_
from github as one feature seams to be not yet released:

.. code::

    pip install -U git+https://github.com/alecthomas/importmagic.git

If using `vim-plug <https://github.com/junegunn/vim-plug>`_ add the following to
``.vimrc`` or ``~/.vim/init.vim``.

.. code::

    Plug 'delijati/vim-imports'
