Documentation
=============

This project is documented using Sphinx.

If needed, the documentation can be locally built, only needing a Python environnement with the appropriate packages installed (see the ``requirements.txt`` file).

To build the documentation locally, run ``make html`` from the ``docs`` directory.
The documentation can then be found in ``docs/_build/html``.

.. warning:: The result differs a bit from the deployed version but the content is the same.

Creating a new documentation
----------------------------

If the needs exists to restart a new documentation, either for tests or another reason, simply create a new empty directory, ``cd`` into it and run ``sphinx-quickstart``.
This will create a new documentation skeleton, which can then be customized.

Base commands are ``make html``, ``make clean html`` and ``sphinx-build source -o output``.

Please refer to the Sphinx documentation for more information.
