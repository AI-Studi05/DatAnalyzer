Continuous Integration
======================

CI is done using GitHub Actions and external services.
It follows the following steps:

* code quality
* tests
* documentation build and deployment
* packaging

The CI is triggered on every push and pull request.

The code quality (and coverage) are using `Coveralls.io <https://coveralls.io/>`_ and `pre-commit.ci <https://results.pre-commit.ci/>`_.

The linter `Action <https://github.com/AI-Studi05/DatAnalyzer/actions/workflows/linter.yml>`_ can be run locally:

.. code-block:: bash

    make lint
