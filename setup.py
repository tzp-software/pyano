try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'pyano',
    'version': '0.5.0',
    'author': 'Kyle Roux',
    'author_email': 'jstacoder@gmail.com',
    'packages': 'payno',
    'description': 'a little python piano',
    'long_description': open('README','r').read(),
}
setup(**config)