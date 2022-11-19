from __future__ import annotations

import zoloto

project = "Zoloto"
copyright = "2020, Jake Howard"  # noqa: A001
author = "Jake Howard"

release = zoloto.__version__

extensions = [
    "sphinx.ext.autodoc",
    "sphinx_autodoc_typehints",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx_rtd_theme",
    "m2r2",
]

templates_path: list[str] = []

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable", None),
}

html_theme = "sphinx_rtd_theme"

html_static_path: list[str] = []

autodoc_default_options = {
    "member-order": "alphabetical",
    "special-members": "__init__, __iter__",
    "undoc-members": True,
    "inherited-members": True,
}

autodoc_mock_imports = ["picamera"]
