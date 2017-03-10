# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os.path
from setuptools import find_packages, setup

# Package data
# ------------
_author = 'COAL Capstone Develeopers'
_author_email = 'coal-capstone@googlegroups.com'
_classifiers = [
    'Environment :: Console',
    'Intended Audience :: Developers',
    'Intended Audience :: Information Technology',
    'Intended Audience :: Science/Research',
    'Topic :: Scientific/Engineering',
    'Development Status :: 1 - Planning',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
]
_description = 'COAL mining library for AVIRIS data.'
_download_url = 'http://pypi.python.org/pypi/pycoal/'
_requirements = ["spectral", "gdal"]
_keywords = ['spectroscopy', 'aviris', 'aviris-ng', 'mining', 'minerals']
_license = 'Apache License, Version 2.0'
_long_description = 'A python suite for the identification and characterization of mining activity within AVIRIS data.'
_name = 'pycoal'
_namespaces = []
_test_suite = 'pycoal.tests'
_url = 'https://github.com/capstone-coal/pycoal'
_version = '0.2'
_zip_safe = False

# Setup Metadata
# --------------


def _read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

_header = '*' * len(_name) + '\n' + _name + '\n' + '*' * len(_name)
_longDescription = '\n\n'.join([
    _header,
    _read('README.md')
])
open('doc.txt', 'w').write(_longDescription)


setup(
    author=_author,
    author_email=_author_email,
    classifiers=_classifiers,
    description=_description,
    download_url=_download_url,
    include_package_data=True,
    install_requires=_requirements,
    keywords=_keywords,
    license=_license,
    long_description=_long_description,
    name=_name,
    namespace_packages=_namespaces,
    packages=find_packages(),
    test_suite=_test_suite,
    url=_url,
    version=_version,
    zip_safe=_zip_safe,
)
