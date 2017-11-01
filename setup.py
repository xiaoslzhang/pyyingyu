import sys
from setuptools import setup,find_packages

def main():
    if sys.version_info <(3,5):
        raise RuntimeError('python 3.0+ is require')
    setup(
        name = 'pyyingyu',
        version = '0.0.3',
        packages = find_packages(),
    )
