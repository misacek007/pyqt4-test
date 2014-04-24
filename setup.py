
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'pyqt4-test',
    'version': '0.1',
    'description': 'My first PyQt4 project',
    'author': 'michal novacek',
    'author_email': 'michal.novacek@gmail.com',
    'url': 'https://github.com/mnovacek-007/pyqt4-test',
    'download_url': 'https://github.com/misacek007/pyqt4-test/archive/master.zip',
    'packages': ['pyqt4-test'],
    'scripts': [],
}

setup(**config)
