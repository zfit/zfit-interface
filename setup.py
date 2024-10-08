#!/usr/bin/env python
from __future__ import annotations

import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "requirements.txt"), encoding="utf-8") as requirements_file:
    requirements = requirements_file.read().splitlines()

with open(os.path.join(here, "requirements_dev.txt"), encoding="utf-8") as requirements_dev_file:
    requirements_dev = requirements_dev_file.read().splitlines()

setup(
    project_urls={
        "Documentation": "https://zfit-interface.readthedocs.io/",
        "Changelog": "https://zfit-interface.readthedocs.io/en/latest/changelog.html",
        "Issue Tracker": "https://github.com/zfit/zfit-interface/issues",
    },
    install_requires=requirements,
    # test_requirements=test_requirements,
    extras_require={"dev": requirements_dev},
    use_scm_version=True,
)
