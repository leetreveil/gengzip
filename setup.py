from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name = 'gengzip',
    version = '0.2.2',
    py_modules=['gengzip'],
    author = 'Lee Treveil',
    author_email = 'leetreveil@gmail.com',
    description = 'A python module for gzipping data using generators',
    long_description=readme(),
    licence='MIT',
    url='https://github.com/leetreveil/gengzip',
    keywords = ['gzip', 'generator'],
)