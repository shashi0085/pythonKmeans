
from setuptools import setup

config = {
        'description': 'PROJECT DESCRIPTION',
        'author': 'Nick Foti',
        'url': 'URL':
        'download_url': 'WHERE TO DOWNLOAD IT',
        'author_email': 'nfoti@uw.edu',
        'version': '0.0.1',
        'install_requires': [],
        'packages': ['NAME'],
        'scripts': [],
        'name': 'kmeans'
}

# Add in any extra build steps for cython, etc.

setup(**config)
