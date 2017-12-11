# coding=utf-8

import os
import sys
from setuptools import setup,find_packages
from setuptools.command.test import test as TestCommand

with open('README.md') as fd:
    long_description = fd.read()


def read_version():
    p = os.path.join(os.path.abspath(os.path.dirname(__file__)),'yingyu','version.py')
    with open(p,'rb') as f:
        return f.read().decode('utf-8').split('=')[-1].strip().strip('"')


class PyTest(TestCommand):
    user_options = []
    
    def run(self):
        import subprocess
        errno = subprocess.call([sys.executable,'-m','pytest','tests'])
        raise SystemExit(errno)


def main():
    if sys.version_info <(3,5):
        raise RuntimeError('python 3.0+ is require')
    install_requires =[
        'aiohttp',    
    ]
    tests_requires = install_requires + ['pytest','pytest-aiohttp']
    setup(
        name='yingyu',
        version=read_version(),
        url='http://github.com/xiaoslzhang/yingyu',
        description='translate',
        long_description=long_description,
        author='xiaoslzhang',
        author_email='xiaoslzhang@163.com',
        license='Freeware',
        packages=find_packages(),
        include_package_data=True,
        entry_points={
            'console_scripts':['yingyu = yingyu.cli:main']    
        },
        install_requires=install_requires,
        tests_requires=tests_requires,
        cmdclass={'test':PyTest},
        classfiers=[
            'License::Freeware',
            'Intended Audience::Developers',
            'Programming Language::Python',
            'Programming Language::Python::3',
            'Programming Language::Python::3.5',
            'Topic::Text Processing',
        ],
    )



if __name__ == '__main__':
    main()
