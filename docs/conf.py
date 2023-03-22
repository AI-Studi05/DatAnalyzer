import os
import sys

# configuration file for the sphinx documentation
# all doc available at
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------

project = "DatAnalyzer"
copyright = "2023, Fracheboud Loic, Poncin Clément"
author = "Fracheboud Loic, Poncin Clément"

# -- General configuration ---------------------------------------------------

# root path
sys.path.append(os.path.abspath(".."))

extensions = ["sphinx.ext.autodoc", "sphinx_rtd_theme"]

exclude_patterns = ["README.rst"]

# -- Options for autodoc -----------------------------------------------------

autosummary_generate = True
templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"

# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_rtd_theme"
html_logo = "images/logo.png"
