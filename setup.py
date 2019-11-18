#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import io
import re
import os
import glob
from setuptools import find_packages
from setuptools import setup


def read(*names, **kwargs):
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ) as fh:
        return fh.read()


here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'requirements.txt'), encoding='utf-8') as requirements_file:
    requirements = requirements_file.read().splitlines()

with open(os.path.join(here, 'requirements_dev.txt'), encoding='utf-8') as requirements_dev_file:
    requirements_dev = requirements_dev_file.read().splitlines()

# split the developer requirements into setup and test requirements
if not requirements_dev.count("") == 1 or requirements_dev.index("") == 0:
    raise SyntaxError("requirements_dev.txt has the wrong format: setup and test "
                      "requirements have to be separated by one blank line.")
requirements_dev_split = requirements_dev.index("")

setup_requirements = ["pip>9",
                      "setuptools_scm",
                      "setuptools_scm_git_archive"]
test_requirements = requirements_dev[requirements_dev_split + 1:]  # +1: skip empty line

setup(
    name='zfit-interface',
    license='BSD-3-Clause',
    description='zfit model fitting interface for HEP',
    long_description='%s\n%s' % (
        re.compile('^.. start-badges.*^.. end-badges', re.M | re.S).sub('', read('README.rst')),
        re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGELOG.rst'))
    ),
    author='Jonas Eschle, Albert Puig, Rafael Silva Coutinho, Matthieu Marinangeli',
    author_email='Jonas.Eschle@cern.ch, apuignav@gmail.com, rsilvaco@cern.ch, matthieu.marinangeli@cern.ch',
    url='https://github.com/zfit/zfit-interface',
    packages=find_packages('zfit_interface'),
    package_dir={'': 'zfit_interface'},
    py_modules=[os.path.splitext(os.path.basename(path))[0] for path in glob.glob('zfit_interface/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering :: Physics',
    ],
    project_urls={
        'Documentation': 'https://zfit-interface.readthedocs.io/',
        'Changelog': 'https://zfit-interface.readthedocs.io/en/latest/changelog.html',
        'Issue Tracker': 'https://github.com/zfit/zfit-interface/issues',
    },
    keywords=[
        'model fitting', 'HEP',
    ],
    python_requires='>=3.6',
    install_requires=requirements,
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    use_scm_version=True,

)
