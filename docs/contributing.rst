Contributing
============

Some rules to follow when contributing:
* The *main* branch is protected, please create a new branch and a pull request for your changes
* Follow the commit message and branching guidelines (see below)
* Follow the code style, see the Google Python style `guide <https://google.github.io/styleguide/pyguide.html>`_
* If you add a new feature, please add a test for it

Commiting and branching
-----------------------

The following table shows the different types of commit tags and their meaning.
Please use them in your commit messages.

+------+------------------------------+
| Type | Description                  |
+======+==============================+
| ADD  | something new is added       |
+------+------------------------------+
| REM  | something was removed        |
+------+------------------------------+
| CHG  | something was changed        |
+------+------------------------------+
| FIX  | problem was corrected        |
+------+------------------------------+
| MOV  | something was moved          |
+------+------------------------------+
| NOTE | additional important message |
+------+------------------------------+
| WARN | additional warning message   |
+------+------------------------------+

**Example** "ADD: new get method. MOV: resources"

Name your branches using *dev/amazing_feature* or *hotfix/issue_66*, *gui/input_fields* helps to filter and see what are each branch doing. Is it a test, a hotfix, or even a bug resolution?
There is no limit to the commit messages policy but the basics mentioned here cover many cases.

For more, read `this <https://dev.to/couchcamote/git-branching-name-convention-cch>`_ article.

Doing some work
---------------

One can start to work by setting up the environment and installing the dependencies using the makefile commands.

.. code-block:: bash

    make welcome

This command will setup the Python virtual environment and install pre-commit hooks.
With this package, you won't be able to commit if the code is not formatted correctly (*actually reject the git commit*).

It uses `pre-commit <https://pre-commit.com/>`_ to ensure that the code is formatted correctly.
The configuration is in the ``.pre-commit-config.yaml`` file.
